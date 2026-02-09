from typing import Annotated

from fastapi import APIRouter, HTTPException
from fastapi.params import Query
from starlette.requests import Request

from core.data.postgres import PgSqlDep
from core.schemas.admin_schema import CreateServiceSchema, UpdateServiceSchema
from core.schemas.cookie_settings_schema import JWTCookieDep
from core.utils.anything import Services, Actions
from core.utils.lite_dependencies import Pagination
from core.utils.permissions_controller import require_permission

router = APIRouter(prefix='/services', tags=['Admin - Services'], dependencies=[JWTCookieDep])


@router.get('/all')
@require_permission(Services.access_matrix, Actions.read)
async def get_services_paginated(q_params: Annotated[Pagination, Query()], db: PgSqlDep, request: Request):
    services = await db.permissions.all_services(q_params.limit, q_params.offset)
    return {'services': services}


@router.post('/create')
@require_permission(Services.access_matrix, Actions.create)
async def create_service(body: CreateServiceSchema, db: PgSqlDep, request: Request):
    service_id = await db.permissions.create_service(body.name, body.description)

    if not service_id:
        raise HTTPException(status_code=409, detail='Сервис с таким именем уже существует')

    return {'success': True,'message': f'Сервис "{body.name}" создан','service_id': service_id}


@router.put('/{service_id}')
@require_permission(Services.access_matrix, Actions.update)
async def update_service(service_id: int, body: UpdateServiceSchema, db: PgSqlDep, request: Request):
    updated = await db.permissions.update_service(service_id, body.name, body.description)

    if not updated:
        raise HTTPException(status_code=404, detail='Сервис не найден')

    return {'success': True,'message': f'Сервис {service_id} обновлён'}


@router.delete('/{service_id}')
@require_permission(Services.access_matrix, Actions.delete)
async def delete_service(service_id: int, db: PgSqlDep, request: Request):
    deleted = await db.permissions.delete_service(service_id)

    if not deleted:
        raise HTTPException(status_code=404, detail='Сервис не найден')

    return {'success': True,'message': f'Сервис {service_id} удалён'}
