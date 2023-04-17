import sqlite3
import bcrypt

DB_PATH = "users.db"

def create_users_table():
    with sqlite3.connect(DB_PATH) as conn:
        c = conn.cursor()
        c.execute('''CREATE TABLE IF NOT EXISTS users
                     (username TEXT PRIMARY KEY, password TEXT)''')
        conn.commit()

def create_user(username, password):
    with sqlite3.connect(DB_PATH) as conn:
        c = conn.cursor()
        hashed_password = bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())
        c.execute("INSERT INTO users VALUES (?, ?)", (username, hashed_password))
        conn.commit()

def authenticate_user(username, password):
    with sqlite3.connect(DB_PATH) as conn:
        c = conn.cursor()
        c.execute("SELECT password FROM users WHERE username=?", (username,))
        row = c.fetchone()
        if row is not None:
            hashed_password = row[0]
            if bcrypt.checkpw(password.encode("utf-8"), hashed_password):
                return True
    return False
