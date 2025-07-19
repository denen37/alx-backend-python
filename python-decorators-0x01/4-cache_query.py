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

query_cache = {}

def cache_query(func):
    @functools.wraps(func)
    def wrapper(conn, query):
        if query in query_cache:
            print("Fetching from cache")
            return query_cache[query]

        result = func(conn, query)
        query_cache[query] = result  # Cache it
        return result
    return wrapper


@with_db_connection
@cache_query
def fetch_users_with_cache(conn, query):
    cursor = conn.cursor()
    cursor.execute(query)
    return cursor.fetchall()

#### First call will cache the result
users = fetch_users_with_cache(query="SELECT * FROM User")
print(users)

#### Second call will use the cached result
users_again = fetch_users_with_cache(query="SELECT * FROM User")
print(users_again)