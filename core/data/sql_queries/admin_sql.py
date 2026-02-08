from asyncpg import Connection


class AdminQueries:
    def __init__(self, conn: Connection):
        self.conn = conn


    async def get_user_by_email(self, email: str):
        ...

    async def get_user_by_id(self, user_id: int):
        ...


    async def all_services(self, limit, offset):
        query = 'SELECT DISTINCT service FROM permissions LIMIT $1 OFFSET $2'
        res = await self.conn.fetchrow(query, limit, offset)
        return res
