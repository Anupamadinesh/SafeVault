import sqlite3

DB_NAME = "safedata.db"

def execute_query(query, params=()):
    """
    Executes database queries using parameterized inputs
    to prevent SQL injection attacks.
    """
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    # Parameterized query execution (safe from SQL injection)
    cursor.execute(query, params)

    result = cursor.fetchall()
    conn.commit()
    conn.close()
    return result

def initialize_db():
    """
    Initializes the database table used in the application.
    """
    execute_query("""
        CREATE TABLE IF NOT EXISTS vault (
            id INTEGER PRIMARY KEY,
            secret TEXT NOT NULL
        );
    """)
