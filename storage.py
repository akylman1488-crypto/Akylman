import sqlite3
import pandas as pd
import json
import hashlib
from datetime import datetime
import os

class AkylmanStorage:
    def __init__(self, db_name="akylman_core_v4.db"):
        self.db_name = db_name
        self.conn = None
        self.cursor = None
        self._connect()
        self._init_tables()

    def _connect(self):
        try:
            self.conn = sqlite3.connect(self.db_name, check_same_thread=False)
            self.cursor = self.conn.cursor()
            self.cursor.execute("PRAGMA journal_mode=WAL;")
        except sqlite3.Error as e:
            print(f"Database connection error: {e}")

    def _init_tables(self):
        queries = [
            '''CREATE TABLE IF NOT EXISTS sessions (
                session_id TEXT PRIMARY KEY,
                start_time DATETIME,
                subject TEXT,
                user_level TEXT
            )''',
            '''CREATE TABLE IF NOT EXISTS messages (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                session_id TEXT,
                role TEXT,
                content TEXT,
                model_used TEXT,
                timestamp DATETIME,
                tokens_count INTEGER,
                FOREIGN KEY(session_id) REFERENCES sessions(session_id)
            )''',
            '''CREATE TABLE IF NOT EXISTS knowledge_base (
                doc_hash TEXT PRIMARY KEY,
                filename TEXT,
                content TEXT,
                upload_date DATETIME,
                file_size_kb REAL
            )''',
            '''CREATE TABLE IF NOT EXISTS user_preferences (
                setting_key TEXT PRIMARY KEY,
                setting_value TEXT
            )''',
            '''CREATE TABLE IF NOT EXISTS error_logs (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                error_msg TEXT,
                timestamp DATETIME
            )'''
        ]
        
        for q in queries:
            self.cursor.execute(q)
        self.conn.commit()

    def create_session(self, subject, level):
        session_id = hashlib.sha256(f"{datetime.now()}{subject}".encode()).hexdigest()[:16]
        try:
            self.cursor.execute(
                "INSERT INTO sessions (session_id, start_time, subject, user_level) VALUES (?, ?, ?, ?)",
                (session_id, datetime.now(), subject, level)
            )
            self.conn.commit()
            return session_id
        except sqlite3.Error:
            return "default_session"

    def save_message(self, session_id, role, content, model="unknown"):
        token_estimate = len(content.split())
        try:
            self.cursor.execute(
                "INSERT INTO messages (session_id, role, content, model_used, timestamp, tokens_count) VALUES (?, ?, ?, ?, ?, ?)",
                (session_id, role, content, model, datetime.now(), token_estimate)
            )
            self.conn.commit()
        except sqlite3.Error as e:
            self.log_error(str(e))

    def get_chat_history(self, session_id, limit=50):
        try:
            query = "SELECT role, content, timestamp FROM messages WHERE session_id = ? ORDER BY id ASC LIMIT ?"
            self.cursor.execute(query, (session_id, limit))
            rows = self.cursor.fetchall()
            return [{"role": r[0], "content": r[1], "time": r[2]} for r in rows]
        except sqlite3.Error:
            return []

    def save_document(self, filename, text_content):
        doc_hash = hashlib.md5(text_content.encode()).hexdigest()
        size_kb = len(text_content.encode('utf-8')) / 1024
        
        try:
            self.cursor.execute("SELECT doc_hash FROM knowledge_base WHERE doc_hash = ?", (doc_hash,))
            if self.cursor.fetchone():
                return False 
            
            self.cursor.execute(
                "INSERT INTO knowledge_base (doc_hash, filename, content, upload_date, file_size_kb) VALUES (?, ?, ?, ?, ?)",
                (doc_hash, filename, text_content, datetime.now(), size_kb)
            )
            self.conn.commit()
            return True
        except sqlite3.Error as e:
            self.log_error(str(e))
            return False

    def get_full_knowledge_context(self):
        try:
            self.cursor.execute("SELECT content FROM knowledge_base")
            rows = self.cursor.fetchall()
            return "\n\n".join([r[0] for r in rows])
        except sqlite3.Error:
            return ""

    def get_knowledge_stats(self):
        try:
            self.cursor.execute("SELECT COUNT(*), SUM(file_size_kb) FROM knowledge_base")
            res = self.cursor.fetchone()
            return {"count": res[0] or 0, "total_kb": round(res[1] or 0, 2)}
        except:
            return {"count": 0, "total_kb": 0}

    def clear_session_memory(self, session_id):
        self.cursor.execute("DELETE FROM messages WHERE session_id = ?", (session_id,))
        self.conn.commit()

    def wipe_all_data(self):
        tables = ["messages", "sessions", "knowledge_base", "error_logs"]
        for t in tables:
            self.cursor.execute(f"DELETE FROM {t}")
        self.conn.commit()

    def log_error(self, message):
        self.cursor.execute("INSERT INTO error_logs (error_msg, timestamp) VALUES (?, ?)", (message, datetime.now()))
        self.conn.commit()

    def get_usage_analytics(self):
        stats = {}
        try:
            self.cursor.execute("SELECT COUNT(*) FROM messages WHERE role='user'")
            stats['user_msgs'] = self.cursor.fetchone()[0]
            
            self.cursor.execute("SELECT COUNT(*) FROM messages WHERE role='assistant'")
            stats['ai_msgs'] = self.cursor.fetchone()[0]
            
            self.cursor.execute("SELECT model_used, COUNT(*) FROM messages WHERE role='assistant' GROUP BY model_used")
            stats['models'] = dict(self.cursor.fetchall())
            
        except:
            stats = {'error': 'Could not retrieve stats'}
        return stats

    def export_history_json(self, session_id):
        history = self.get_chat_history(session_id, limit=1000)
        return json.dumps(history, ensure_ascii=False, indent=4)

    def close(self):
        if self.conn:
            self.conn.close()
