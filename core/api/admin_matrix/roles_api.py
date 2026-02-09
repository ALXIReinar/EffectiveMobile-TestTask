from typing import Annotated

from fastapi import APIRouter, HTTPException
from fastapi.params import Query
from starlette.requests import Request

from core.data.postgres import PgSqlDep
from core.schemas.admin_schema import AddRemovePermSchema, CreateRoleSchema, UpdateRoleSchema
from core.utils.anything import Services, Actions
from core.utils.lite_dependencies import Pagination
from core.utils.permissions_controller import require_permission

router = APIRouter(prefix='/roles', tags=['Admin - Roles'])



"Работа с ролями + привилегиями"
@router.post('/add_permission')
@require_permission(Services.access_matrix, Actions.create)
async def add_permission_to_role(body: AddRemovePermSchema, db: PgSqlDep, request: Request):
    await db.permissions.add_permission_to_role(body.role, body.permission_id)
    return {'success': True, 'message': f'Привилегия {body.permission_id} добавлена роли {body.role}'}


@router.delete('/remove_permission')
@require_permission(Services.access_matrix, Actions.delete)
async def remove_permission_from_role(body: AddRemovePermSchema, db: PgSqlDep, request: Request):
    await db.permissions.remove_permission_from_role(body.role, body.permission_id)
    return {'success': True, 'message': f'Привилегия {body.permission_id} отозвана у роли {body.role}'}



"Непосредственно роли"
@router.get('/all')
@require_permission(Services.access_matrix, Actions.read)
async def get_all_roles(q_params: Annotated[Pagination, Query()], db: PgSqlDep, request: Request):
    roles = await db.permissions.get_all_roles(q_params.limit, q_params.offset)
    return {'roles': roles}


@router.get('/{role}')
@require_permission(Services.access_matrix, Actions.read)
async def get_role_permissions(role: str, db: PgSqlDep, request: Request):
    permissions = await db.permissions.get_role_permissions(role)
    return {'role': role, 'permissions': permissions}


@router.post('/create')
@require_permission(Services.access_matrix, Actions.create)
async def create_role(body: CreateRoleSchema, db: PgSqlDep, request: Request):
    role_id = await db.permissions.create_role(body.name, body.description)

    if not role_id:
        raise HTTPException(status_code=409, detail='Роль с таким именем уже существует')

    return {'success': True,'message': f'Роль "{body.name}" создана','role_id': role_id}


@router.put('/{role_id}')
@require_permission(Services.access_matrix, Actions.update)
async def update_role(role_id: int, body: UpdateRoleSchema, db: PgSqlDep, request: Request):
    updated = await db.permissions.update_role(role_id, body.name, body.description)

    if not updated:
        raise HTTPException(status_code=404, detail='Роль не найдена')

    return {'success': True,'message': f'Роль {role_id} обновлена'}


@router.delete('/{role_id}')
@require_permission(Services.access_matrix, Actions.delete)
async def delete_role(role_id: int, db: PgSqlDep, request: Request):
    deleted = await db.permissions.delete_role(role_id)

    if not deleted:
        raise HTTPException(status_code=404, detail='Роль не найдена')

    return {'success': True,'message': f'Роль {role_id} удалена'}
