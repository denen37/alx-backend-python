import sqlite3
import functools

def with_db_connection(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        conn = sqlite3.connect('C:/Users/HP/source/db/alx-airbnb.db')
        print('Database connection opened')
        try:
            return func(conn, *args, **kwargs)
        finally:
            conn.close()
            print('Database connection closed')
    return wrapper

@with_db_connection 
def get_user_by_id(conn, user_id): 
    cursor = conn.cursor() 
    cursor.execute("SELECT * FROM User WHERE user_id = ?", (user_id,)) 
    return cursor.fetchone() 
#### Fetch user by ID with automatic connection handling 

user = get_user_by_id(user_id='u1111111-1111-4111-a111-111111111114')
print(user)



