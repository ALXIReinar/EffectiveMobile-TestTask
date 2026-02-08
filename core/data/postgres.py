from typing import Annotated

from asyncpg import Connection
from fastapi.params import Depends
from starlette.requests import Request

from core.data.sql_queries.admin_sql import AdminQueries
from core.data.sql_queries.users_sql import UsersQueries, AuthQueries
from core.data.sql_queries.permissions_sql import PermissionsQueries


class PgSql:
    def __init__(self, conn: Connection):
        self.conn = conn
        self.users = UsersQueries(conn)
        self.auth = AuthQueries(conn)
        self.admin = AdminQueries(conn)
        self.permissions = PermissionsQueries(conn)



async def get_pg_pool(request: Request):
    async with request.app.state.pg_pool.acquire() as conn:
        yield conn

async def get_custom_pgsql(conn: Annotated[Connection, Depends(get_pg_pool)]):
    yield PgSql(conn)

PgSqlDep = Annotated[PgSql, Depends(get_custom_pgsql)]
