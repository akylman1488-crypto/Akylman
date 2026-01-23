import sqlite3
import pandas as pd
import json
import os
from datetime import datetime

class AkylmanStorage:
    def __init__(self, db_name="akylman_vault.db"):
        self.db_name = db_name
        self.init_database()

    def init_database(self):
        conn = sqlite3.connect(self.db_name, check_same_thread=False)
        c = conn.cursor()
        
        c.execute('''CREATE TABLE IF NOT EXISTS chat_history 
                     (id INTEGER PRIMARY KEY AUTOINCREMENT, 
                      subject TEXT, 
                      role TEXT, 
                      content TEXT, 
                      timestamp DATETIME)''')
        
        c.execute('''CREATE TABLE IF NOT EXISTS user_profile 
                     (key TEXT PRIMARY KEY, 
                      value TEXT)''')
        
        c.execute('''CREATE TABLE IF NOT EXISTS document_index 
                     (doc_name TEXT PRIMARY KEY, 
                      content TEXT, 
                      upload_date DATETIME)''')
        
        c.execute('''CREATE TABLE IF NOT EXISTS metrics 
                     (metric_name TEXT PRIMARY KEY, 
                      count INTEGER DEFAULT 0)''')
        
        conn.commit()
        conn.close()

    def save_message(self, subject, role, content):
        conn = sqlite3.connect(self.db_name)
        c = conn.cursor()
        c.execute("INSERT INTO chat_history (subject, role, content, timestamp) VALUES (?, ?, ?, ?)", 
                  (subject, role, content, datetime.now()))
        
        c.execute("INSERT OR IGNORE INTO metrics (metric_name, count) VALUES ('total_messages', 0)")
        c.execute("UPDATE metrics SET count = count + 1 WHERE metric_name = 'total_messages'")
        
        conn.commit()
        conn.close()

    def get_history(self, subject, limit=50):
        conn = sqlite3.connect(self.db_name)
        df = pd.read_sql_query("SELECT role, content FROM chat_history WHERE subject = ? ORDER BY timestamp DESC LIMIT ?", 
                               conn, params=(subject, limit))
        conn.close()
        return df.iloc[::-1].to_dict('records')

    def clear_subject_history(self, subject):
        conn = sqlite3.connect(self.db_name)
        c = conn.cursor()
        c.execute("DELETE FROM chat_history WHERE subject = ?", (subject,))
        conn.commit()
        conn.close()

    def save_document(self, name, text):
        conn = sqlite3.connect(self.db_name)
        c = conn.cursor()
        c.execute("INSERT OR REPLACE INTO document_index (doc_name, content, upload_date) VALUES (?, ?, ?)", 
                  (name, text, datetime.now()))
        conn.commit()
        conn.close()

    def get_all_documents(self):
        conn = sqlite3.connect(self.db_name)
        df = pd.read_sql_query("SELECT doc_name FROM document_index", conn)
        conn.close()
        return df['doc_name'].tolist()

    def get_document_content(self, name):
        conn = sqlite3.connect(self.db_name)
        c = conn.cursor()
        c.execute("SELECT content FROM document_index WHERE doc_name = ?", (name,))
        res = c.fetchone()
        conn.close()
        return res[0] if res else ""

    def update_user_setting(self, key, value):
        conn = sqlite3.connect(self.db_name)
        c = conn.cursor()
        c.execute("INSERT OR REPLACE INTO user_profile (key, value) VALUES (?, ?)", (key, str(value)))
        conn.commit()
        conn.close()

    def get_user_setting(self, key, default=None):
        conn = sqlite3.connect(self.db_name)
        c = conn.cursor()
        c.execute("SELECT value FROM user_profile WHERE key = ?", (key,))
        res = c.fetchone()
        conn.close()
        return res[0] if res else default

    def get_stats(self):
        conn = sqlite3.connect(self.db_name)
        c = conn.cursor()
        c.execute("SELECT count FROM metrics WHERE metric_name = 'total_messages'")
        msg_count = c.fetchone()
        
        c.execute("SELECT COUNT(DISTINCT subject) FROM chat_history")
        subj_count = c.fetchone()
        
        conn.close()
        return {
            "messages": msg_count[0] if msg_count else 0,
            "subjects": subj_count[0] if subj_count else 0
        }

    def export_to_json(self, filename="backup.json"):
        conn = sqlite3.connect(self.db_name)
        df = pd.read_sql_query("SELECT * FROM chat_history", conn)
        df.to_json(filename, orient='records', force_ascii=False)
        conn.close()
        return filename

    def delete_all_data(self):
        if os.path.exists(self.db_name):
            os.remove(self.db_name)
            self.init_database()
            return True
        return False

  
