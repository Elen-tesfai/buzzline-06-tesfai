import sqlite3
from sqlite3 import Error

# Establish a connection to the database
def create_connection(db_file):
    """ Create a database connection to the SQLite database """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print(f"Connected to SQLite version {sqlite3.version}")
    except Error as e:
        print(f"Error: {e}")
    return conn

# Create a table if it doesn't already exist
def create_table(conn):
    """ Create a table to store processed sentiment data """
    try:
        sql_create_table = """
        CREATE TABLE IF NOT EXISTS sentiment_data (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp TEXT NOT NULL,
            author TEXT NOT NULL,
            content TEXT NOT NULL,
            category TEXT NOT NULL,
            sentiment_score REAL,
            message_length INTEGER
        );
        """
        cursor = conn.cursor()
        cursor.execute(sql_create_table)
        print("Table created or already exists.")
    except Error as e:
        print(f"Error: {e}")

# Insert sentiment data into the table
def insert_sentiment_data(conn, sentiment_data):
    """ Insert processed sentiment data into the database """
    try:
        sql_insert = """
        INSERT INTO sentiment_data (timestamp, author, content, category, sentiment_score, message_length)
        VALUES (?, ?, ?, ?, ?, ?)
        """
        cursor = conn.cursor()
        cursor.execute(sql_insert, sentiment_data)
        conn.commit()
        print(f"Inserted data: {sentiment_data}")
    except Error as e:
        print(f"Error: {e}")