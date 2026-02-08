from typing import Annotated

from fastapi import APIRouter
from fastapi.params import Query

from core.data.postgres import PgSqlDep
from core.schemas.admin_schema import AddRemovePermSchema
from core.utils.anything import Permissions
from core.utils.lite_dependencies import Pagination
from core.utils.permissions_controller import require_permission

router = APIRouter(prefix='/private/admin', tags=['Admin'])


"Сервисы"
@router.get('/all_services')
async def get_all_services(q_params: Annotated[Pagination, Query()], db: PgSqlDep):
    """Получить все сервисы"""
    services = await db.admin.all_services(q_params.limit, q_params.offset)
    return {'services' : services}


"Пользователи"
@router.get('/permissions')
async def all_permissions(q_params: Annotated[Pagination, Query()], db: PgSqlDep):
    """Получить все доступные разрешения"""
    permissions = await db.permissions.get_all_permissions()
    return {'permissions': permissions}


@router.get('/users')
@require_permission('users', Permissions.read)
async def get_users_list():
    """Список пользователей (доступно: admin, hr, security)"""
    return {
        'service': 'users',
        'users': [
            {'id': 1, 'email': 'admin@company.com', 'role': 'admin'},
            {'id': 2, 'email': 'dev@company.com', 'role': 'developer'}
        ]
    }


@router.post('/users')
@require_permission('users', 'create')
async def create_user():
    """Создать пользователя (доступно: admin, hr)"""
    return {'service': 'users', 'message': 'User created'}


@router.delete('/users/{user_id}')
@require_permission('users', 'delete')
async def delete_user(user_id: int):
    """Удалить пользователя (доступно: admin)"""
    return {'service': 'users', 'message': f'User {user_id} deleted'}


"Привилегии"
@router.get('/permissions/role/{role}')
async def api_get_role_permissions(role: str, db: PgSqlDep):
    """Получить все разрешения для конкретной роли"""
    permissions = await db.permissions.get_role_permissions(role)
    return {'role': role, 'permissions': permissions}


@router.post('/permissions/role/{role}/add')
async def add_permission2role(body: AddRemovePermSchema, db: PgSqlDep):
    """Добавить разрешение роли"""
    await db.permissions.add_permission_to_role(body.role, body.permission_id)
    return {'success': True, 'message': f'Привилегия {body.permission_id} добавлена роли {body.role}'}


@router.delete('/permissions/role/{role}/remove')
async def api_remove_permission_from_role(body: AddRemovePermSchema, db: PgSqlDep):
    """Отозвать разрешение у роли"""
    await db.permissions.remove_permission_from_role(body.role, body.permission_id)
    return {'success': True, 'message': f'Привилегия {body.permission_id} отозвана у роли {body.role}'}
