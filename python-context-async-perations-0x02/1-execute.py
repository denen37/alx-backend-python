import sqlite3

class ExecuteQuery:
    def __init__(self, query, *args):
        self.db = 'C:/Users/HP/source/db/alx-airbnb.db'
        self.query = query
        self.args = args

    def __enter__(self):
        self.conn = sqlite3.connect(self.db)
        print('Database connection opened')

        cursor = self.conn.cursor()
        cursor.execute(self.query, self.args)
        return cursor.fetchone()

    def __exit__(self, exc_type, exc_value, traceback):
        self.conn.close()
        print('Database connection closed')


with ExecuteQuery('SELECT * FROM User WHERE email = ?', 'john.doe1@example.com') as exec_query:
    print(exec_query)