from asyncpg import Connection


class AdminQueries:
    def __init__(self, conn: Connection):
        self.conn = conn

    async def all_services(self, limit, offset):
        query = 'SELECT id, name, description FROM services LIMIT $1 OFFSET $2'
        res = await self.conn.fetch(query, limit, offset)
        return res

