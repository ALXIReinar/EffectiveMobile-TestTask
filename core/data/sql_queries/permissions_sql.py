from asyncpg import Connection


class PermissionsQueries:
    def __init__(self, conn: Connection):
        self.conn = conn

    async def check_permission(self, role_id: int, service_id: int, action_id: int) -> bool:
        """
        Проверяет, есть ли у роли разрешение (использует id для производительности)
        Используется в декораторе @require_permission
        
        Args:
            role_id: название роли (например, 'developer')
            service_id: ID сервиса из Services датакласса
            action_id: ID действия из Permissions датакласса
        """
        query = '''
        SELECT 1 
        FROM role_permissions rp
        JOIN permissions p ON rp.permission_id = p.id
        WHERE rp.role_id = $1 AND p.service_id = $2 AND p.action_id = $3
        '''
        res = await self.conn.fetchval(query, role_id, service_id, action_id)
        return res


    async def get_role_permissions(self, role: str):
        query = '''
        SELECT s.id as service_id, s.name as service, a.id as action_id, a.name as action, p.description
        FROM role_permissions rp
        JOIN permissions p ON rp.permission_id = p.id
        JOIN roles r ON rp.role_id = r.id
        JOIN services s ON p.service_id = s.id
        JOIN actions a ON p.action_id = a.id
        WHERE r.name = $1
        '''
        res = await self.conn.fetch(query, role)
        return res


    async def get_all_permissions(self, limit: int, offset: int):
        query = '''
        SELECT p.id, s.name as service, a.name as action, p.description
        FROM permissions p
        JOIN services s ON p.service_id = s.id
        JOIN actions a ON p.action_id = a.id
        LIMIT $1 OFFSET $2
        '''
        res = await self.conn.fetch(query, limit, offset)
        return res


    async def add_permission_to_role(self, role: str, permission_id: int):
        query = '''
        INSERT INTO role_permissions (role_id, permission_id)
        SELECT r.id, $2 FROM roles r
        WHERE r.name = $1
        ON CONFLICT (role_id, permission_id) DO NOTHING
        '''
        await self.conn.execute(query, role, permission_id)


    async def remove_permission_from_role(self, role: str, permission_id: int):
        query = '''
        DELETE FROM role_permissions 
        WHERE role_id = (SELECT id FROM roles WHERE name = $1)
          AND permission_id = $2
        
        '''
        await self.conn.execute(query, role, permission_id)


    async def get_all_roles(self, limit: int, offset: int):
        query = 'SELECT id, name, description FROM roles LIMIT $1 OFFSET $2'
        res = await self.conn.fetch(query, limit, offset)
        return res
    

    async def all_services(self, limit, offset):
        query = 'SELECT id, name, description FROM services LIMIT $1 OFFSET $2'
        res = await self.conn.fetch(query, limit, offset)
        return res


    async def get_all_actions(self, limit: int, offset: int):
        """Получить все действия с пагинацией"""
        query = 'SELECT id, name, description FROM actions ORDER BY name LIMIT $1 OFFSET $2'
        res = await self.conn.fetch(query, limit, offset)
        return res
    
    async def create_action(self, name: str, description: str):
        """Создать новое действие"""
        query = '''
        INSERT INTO actions (name, description)
        VALUES ($1, $2)
        ON CONFLICT (name) DO NOTHING
        RETURNING id
        '''
        res = await self.conn.fetchval(query, name, description)
        return res
    
    async def update_action(self, action_id: int, name: str, description: str):
        """Обновить действие"""
        query = '''
        UPDATE actions
        SET name = $2, description = $3
        WHERE id = $1
        RETURNING id
        '''
        res = await self.conn.fetchval(query, action_id, name, description)
        return res is not None
    
    async def delete_action(self, action_id: int):
        """Удалить действие (каскадно удалит связанные permissions)"""
        query = 'DELETE FROM actions WHERE id = $1 RETURNING id'
        res = await self.conn.fetchval(query, action_id)
        return res is not None


    async def create_service(self, name: str, description: str):
        """Создать новый сервис"""
        query = '''
        INSERT INTO services (name, description)
        VALUES ($1, $2)
        ON CONFLICT (name) DO NOTHING
        RETURNING id
        '''
        res = await self.conn.fetchval(query, name, description)
        return res
    
    async def update_service(self, service_id: int, name: str, description: str):
        """Обновить сервис"""
        query = '''
        UPDATE services
        SET name = $2, description = $3
        WHERE id = $1
        RETURNING id
        '''
        res = await self.conn.fetchval(query, service_id, name, description)
        return res is not None
    
    async def delete_service(self, service_id: int):
        """Удалить сервис (каскадно удалит связанные permissions)"""
        query = 'DELETE FROM services WHERE id = $1 RETURNING id'
        res = await self.conn.fetchval(query, service_id)
        return res is not None


    async def create_permission(self, service_id: int, action_id: int, description: str):
        """Создать новое разрешение (service + action)"""
        query = '''
        INSERT INTO permissions (service_id, action_id, description)
        VALUES ($1, $2, $3)
        ON CONFLICT (service_id, action_id) DO NOTHING
        RETURNING id
        '''
        res = await self.conn.fetchval(query, service_id, action_id, description)
        return res
    
    async def update_permission(self, permission_id: int, description: str):
        """Обновить описание разрешения"""
        query = '''
        UPDATE permissions
        SET description = $2
        WHERE id = $1
        RETURNING id
        '''
        res = await self.conn.fetchval(query, permission_id, description)
        return res is not None
    
    async def delete_permission(self, permission_id: int):
        """Удалить разрешение (каскадно удалит связи с ролями)"""
        query = 'DELETE FROM permissions WHERE id = $1 RETURNING id'
        res = await self.conn.fetchval(query, permission_id)
        return res is not None


    async def create_role(self, name: str, description: str):
        """Создать новую роль"""
        query = '''
        INSERT INTO roles (name, description)
        VALUES ($1, $2)
        ON CONFLICT (name) DO NOTHING
        RETURNING id
        '''
        res = await self.conn.fetchval(query, name, description)
        return res
    
    async def update_role(self, role_id: int, name: str, description: str):
        """Обновить роль"""
        query = '''
        UPDATE roles
        SET name = $2, description = $3
        WHERE id = $1
        RETURNING id
        '''
        res = await self.conn.fetchval(query, role_id, name, description)
        return res is not None
    
    async def delete_role(self, role_id: int):
        """Удалить роль (каскадно удалит связи с permissions)"""
        query = 'DELETE FROM roles WHERE id = $1 RETURNING id'
        res = await self.conn.fetchval(query, role_id)
        return res is not None

