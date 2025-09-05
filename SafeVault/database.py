import sqlite3

DB_NAME = "safedata.db"

def execute_query(query, params=()):
    """
    Executes parameterized queries to prevent SQL injection.
    """
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute(query, params)
    result = cursor.fetchall()
    conn.commit()
    conn.close()
    return result

# Example: create a table for demo
def initialize_db():
    execute_query("""
    CREATE TABLE IF NOT EXISTS vault (
        id INTEGER PRIMARY KEY,
        secret TEXT NOT NULL
    );
    """)
