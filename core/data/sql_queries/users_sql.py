from asyncpg import Connection

from core.config_dir.config import encryption


class UsersQueries:
    def __init__(self, conn: Connection):
        self.conn = conn

    async def reg_user(self, email, passw: str, first_name: str, surname: str, last_name: str, role_id: int):
        query = '''
        INSERT INTO users (email, passw, first_name, surname, last_name, role_id, is_active)
        VALUES($1, $2, $3, $4, $5, $6, true)
        ON CONFLICT (email) WHERE is_active = true DO NOTHING 
        RETURNING id
        '''
        hashed = encryption.hash(passw)

        res = await self.conn.fetchval(query, email, hashed, first_name, surname, last_name, role_id)
        return res

    async def select_user(self, email):
        query = 'SELECT id, passw, role_id FROM users WHERE email = $1 AND is_active = true'
        res = await self.conn.fetchrow(query, email)
        return res



class AuthQueries:
    def __init__(self, conn: Connection):
        self.conn = conn

    async def make_session(
            self,
            session_id: str,
            user_id: int,
            iat: int,
            exp: int,
            user_agent: str,
            ip: str,
            hashed_rT: str
    ):
        query = '''
        INSERT INTO sessions_users (session_id, user_id, iat, exp, refresh_token, user_agent, ip) VALUES($1,$2,$3,$4,$5,$6,$7)
        ON CONFLICT (session_id) DO UPDATE SET  iat = $3, exp = $4, refresh_token = $5, ip = $7
        '''
        await self.conn.execute(query, session_id, user_id, iat, exp, hashed_rT, user_agent, ip)


    async def get_actual_rt(self, user_id: int, session_id: str):
        query = 'SELECT refresh_token FROM sessions_users WHERE user_id = $1 AND session_id = $2 AND "exp" > now()'
        res = await self.conn.fetchrow(query, user_id, session_id)
        return res


    async def check_exist_session(self, user_id: int, user_agent: str):
        query = '''
        SELECT session_id FROM public.sessions_users WHERE user_id = $1 AND user_agent = $2
        '''
        res = await self.conn.fetchrow(query, user_id, user_agent)
        return res

    async def session_termination(self, user_id: int, session_id: str):
        query = 'DELETE FROM sessions_users WHERE user_id = $1 AND session_id = $2'
        await self.conn.execute(query, user_id, session_id)


    async def delete_account(self, user_id: int):
        query = '''
        WITH sessions_users AS (
            DELETE FROM sessions_users WHERE user_id = $1
        )
        UPDATE users SET is_active = false WHERE id = $1
        '''
        await self.conn.execute(query, user_id)