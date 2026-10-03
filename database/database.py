import aiosqlite

DB_PATH = "database/olympus.db"

async def init_db():
    async with aiosqlite.connect(DB_PATH) as db:
        await db.execute("""CREATE TABLE IF NOT EXISTS transactions (
            id TEXT PRIMARY KEY,
            service TEXT NOT NULL,
            user_id INTEGER NOT NULL,
            amount TEXT,
            payment_method TEXT,
            status TEXT NOT NULL,
            created_at TEXT NOT NULL,
            completed_at TEXT
        )""")
        await db.commit()
