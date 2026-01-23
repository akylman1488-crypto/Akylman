import sqlite3
import pandas as pd

class AkylmanStorage:
    def __init__(self):
        self.conn = sqlite3.connect('akylman_v4.db', check_same_thread=False)
        self.create_tables()

    def create_tables(self):
        c = self.conn.cursor()
        c.execute('''CREATE TABLE IF NOT EXISTS history 
                     (id INTEGER PRIMARY KEY, level TEXT, role TEXT, content TEXT, sub TEXT)''')
        self.conn.commit()

    def add_msg(self, level, role, content, sub):
        c = self.conn.cursor()
        c.execute("INSERT INTO history (level, role, content, sub) VALUES (?, ?, ?, ?)", 
                  (level, role, content, sub))
        self.conn.commit()

    def load_history(self, sub):
        return pd.read_sql_query(f"SELECT role, content FROM history WHERE sub='{sub}'", self.conn)
