import sqlite3
from datetime import datetime

DB_FILE = "messages.db"

def init_db():
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute("""
        CREATE TABLE IF NOT EXISTS logs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            direction TEXT,
            peer TEXT,
            message TEXT,
            timestamp TEXT
        )
    """)
    conn.commit()
    conn.close()

def log_message(direction: str, peer: str, message: str):
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    timestamp = datetime.now().isoformat()
    c.execute("INSERT INTO logs (direction, peer, message, timestamp) VALUES (?, ?, ?, ?)",
              (direction, peer, message, timestamp))
    conn.commit()
    conn.close()
