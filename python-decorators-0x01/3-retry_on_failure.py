import time
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

# Decorator factory for retries
def retry_on_failure(retries=3, delay=1):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(conn, *args, **kwargs):
            for i in range(retries):
                try:
                    return func(conn, *args, **kwargs)
                except Exception as e:
                    print(f'Attempt {i + 1} failed: {e}')
                    if i + 1 < retries:
                        print(f'Retrying after {delay} seconds...')
                        time.sleep(delay)
                    else:
                        print(f'All {retries} attempts failed.')
                        raise Exception(f'Operation failed after {retries} attempts') from e
        return wrapper
    return decorator

@with_db_connection
@retry_on_failure(retries=3, delay=1)
def fetch_users_with_retry(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users")
    return cursor.fetchall()

# Call function
users = fetch_users_with_retry()
print(users)
