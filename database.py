import sqlite3

def init_db():
    conn = sqlite3.connect("notes.db")
    cursor = conn.cursor()
    
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS notes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        original TEXT,
        summary TEXT
    )
    """)
    
    conn.commit()
    conn.close()

def save_note(original, summary):
    conn = sqlite3.connect("notes.db")
    cursor = conn.cursor()

    cursor.execute("""CREATE TABLE IF NOT EXISTS notes (id INTEGER PRIMARY KEY AUTOINCREMENT, original TEXT, summary TEXT)""")
    
    cursor.execute("INSERT INTO notes (original, summary) VALUES (?, ?)", 
                   (original, summary))
    
    conn.commit()
    conn.close()

def get_notes():
    conn = sqlite3.connect("notes.db")
    cursor = conn.cursor()
    
    cursor.execute("SELECT * FROM notes")
    data = cursor.fetchall()
    
    conn.close()
    return data