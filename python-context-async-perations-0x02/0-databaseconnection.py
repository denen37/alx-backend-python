import sqlite3

class DatabaseConnection:
    def __init__(self):
        self.db = 'C:/Users/HP/source/db/alx-airbnb.db'
    def __enter__(self):
        self.conn = sqlite3.connect(self.db)
        print('Database connection opened')
        return self.conn
    def __exit__(self, exc_type, exc_value, traceback):
        self.conn.close()
        print('Database connection closed')

def run_query(query):
    with DatabaseConnection() as dbconn:
        cursor = dbconn.cursor()
        cursor.execute(query)
        return cursor.fetchone()

result = run_query("SELECT * FROM users")
print(result)