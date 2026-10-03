from database.database import DB_PATH
import aiosqlite

async def get_transaction(transaction_id: str):
    async with aiosqlite.connect(DB_PATH) as db:
        db.row_factory = aiosqlite.Row
        async with db.execute("SELECT * FROM transactions WHERE id = ?", (transaction_id,)) as cursor:
            row = await cursor.fetchone()
            return dict(row) if row else None
