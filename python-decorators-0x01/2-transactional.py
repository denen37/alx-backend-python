import sqlite3
import functools

# Decorator to handle DB connection
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

# Decorator to handle transactions
def transactional(func):
    @functools.wraps(func)
    def wrapper(conn, *args, **kwargs):
        try:
            print("Begin Transaction")
            conn.execute("BEGIN")
            result = func(conn, *args, **kwargs)
            conn.commit()
            print("Commit Transaction")
            return result
        except Exception as e:
            conn.rollback()
            print("Rollback Transaction:", e)
            raise  # Optional: re-raise the exception
    return wrapper

# Function using both decorators
@with_db_connection
@transactional
def update_user_email(conn, user_id, new_email):
    cursor = conn.cursor()
    cursor.execute("UPDATE users SET email = ? WHERE id = ?", (new_email, user_id))
    print(f"Updated user {user_id}'s email to {new_email}")

# Call the function
update_user_email(user_id=1, new_email='Crawford_Cartwright@hotmail.com')
