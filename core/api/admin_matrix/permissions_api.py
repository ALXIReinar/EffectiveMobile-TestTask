from typing import Annotated

from fastapi import APIRouter, HTTPException
from fastapi.params import Query
from starlette.requests import Request

from core.data.postgres import PgSqlDep
from core.schemas.admin_schema import CreatePermissionSchema, UpdatePermissionSchema
from core.utils.anything import Services, Actions
from core.utils.lite_dependencies import Pagination
from core.utils.permissions_controller import require_permission

router = APIRouter(prefix='/permissions', tags=['Admin - Permissions'])


@router.get('/all')
@require_permission(Services.access_matrix, Actions.read)
async def all_permissions(q_params: Annotated[Pagination, Query()], db: PgSqlDep, request: Request):
    permissions = await db.permissions.get_all_permissions(q_params.limit, q_params.offset)
    return {'permissions': permissions}


@router.post('/create')
@require_permission(Services.access_matrix, Actions.create)
async def create_permission(body: CreatePermissionSchema, db: PgSqlDep, request: Request):
    permission_id = await db.permissions.create_permission(body.service_id,body.action_id,body.description)

    if not permission_id:
        raise HTTPException(status_code=409, detail='Разрешение для этой комбинации service+action уже существует')

    return {'success': True,'message': 'Разрешение создано','permission_id': permission_id}


@router.put('/{permission_id}')
@require_permission(Services.access_matrix, Actions.update)
async def update_permission(permission_id: int, body: UpdatePermissionSchema, db: PgSqlDep, request: Request):
    updated = await db.permissions.update_permission(permission_id, body.description)

    if not updated:
        raise HTTPException(status_code=404, detail='Разрешение не найдено')

    return {'success': True,'message': f'Разрешение {permission_id} обновлено'}


@router.delete('/{permission_id}')
@require_permission(Services.access_matrix, Actions.delete)
async def delete_permission(permission_id: int, db: PgSqlDep, request: Request):
    deleted = await db.permissions.delete_permission(permission_id)

    if not deleted:
        raise HTTPException(status_code=404, detail='Разрешение не найдено')

    return {'success': True,'message': f'Разрешение {permission_id} удалено'}
