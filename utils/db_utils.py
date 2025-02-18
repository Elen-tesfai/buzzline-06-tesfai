import sqlite3

def create_connection(db_file):
    """Create a connection to the SQLite database."""
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except sqlite3.Error as e:
        print(e)
    return conn


def create_table(conn):
    """Create a table in the SQLite database."""
    try:
        create_table_sql = '''CREATE TABLE IF NOT EXISTS messages (
                                id INTEGER PRIMARY KEY,
                                timestamp TEXT NOT NULL,
                                author TEXT NOT NULL,
                                content TEXT NOT NULL,
                                category TEXT NOT NULL,
                                sentiment_score REAL NOT NULL,
                                message_length INTEGER NOT NULL
                            );'''
        cursor = conn.cursor()
        cursor.execute(create_table_sql)
    except sqlite3.Error as e:
        print(e)


def insert_message(conn, timestamp, author, content, category, sentiment_score, message_length):
    """Insert a message into the messages table."""
    try:
        insert_sql = '''INSERT INTO messages (timestamp, author, content, category, sentiment_score, message_length)
                        VALUES (?, ?, ?, ?, ?, ?);'''
        cursor = conn.cursor()
        cursor.execute(insert_sql, (timestamp, author, content, category, sentiment_score, message_length))
        conn.commit()
    except sqlite3.Error as e:
        print(f"Error inserting message: {e}")