from asyncpg import Connection


class AdminQueries:
    def __init__(self, conn: Connection):
        self.conn = conn


    async def get_user_by_email(self, email: str):
        ...

    async def get_user_by_id(self, user_id: int):
        ...


    async def all_services(self):

        ... # Запрос в таблицу services

        return [    # мок ответ
            {'id': 1, 'title': 'analytics'},
            {'id': 2, 'title': 'development'},
            {'id': 3, 'title': 'HR department'},
        ]
