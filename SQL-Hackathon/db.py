import sqlite3

DB_NAME = "results.db"

def init_db():
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute("""
        CREATE TABLE IF NOT EXISTS results (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp TEXT,
            mode TEXT,
            shape TEXT,
            duration REAL
        )
    """)
    conn.commit()
    conn.close()

def store_result(timestamp, mode, shape, duration):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute("""
        INSERT INTO results (timestamp, mode, shape, duration)
        VALUES (?, ?, ?, ?)
    """, (timestamp, mode, shape, duration))
    conn.commit()
    conn.close()

init_db()
