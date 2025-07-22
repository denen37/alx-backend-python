import asyncio
import aiosqlite

async def async_fetch_users():
    async with aiosqlite.connect('C:/Users/HP/source/db/alx-airbnb.db') as db:
        cursor = await db.execute('SELECT * FROM User')
        rows = await cursor.fetchall()
        return rows

async def async_fetch_older_users():
    async with aiosqlite.connect('C:/Users/HP/source/db/alx-airbnb.db') as db:
        cursor = await db.execute('SELECT * FROM User WHERE age = ?', (40,))
        rows = await cursor.fetchall()
        return rows

async def fetch_concurrently():
    users, older_users = await asyncio.gather(
        async_fetch_users(),
        async_fetch_older_users()
    )
    return users, older_users

# Run the async function
users, older_users = asyncio.run(fetch_concurrently())

print("All Users:")
print(users)

print("\nOlder Users:")
print(older_users)
