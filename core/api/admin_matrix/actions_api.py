from typing import Annotated

from fastapi import APIRouter, HTTPException
from fastapi.params import Query
from starlette.requests import Request

from core.data.postgres import PgSqlDep
from core.schemas.admin_schema import CreateActionSchema, UpdateActionSchema
from core.schemas.cookie_settings_schema import JWTCookieDep
from core.utils.anything import Services, Actions
from core.utils.lite_dependencies import Pagination
from core.utils.permissions_controller import require_permission

router = APIRouter(prefix='/actions', tags=['Admin - Actions'], dependencies=[JWTCookieDep])



@router.get('/all')
@require_permission(Services.access_matrix, Actions.read)
async def get_all_actions(q_params: Annotated[Pagination, Query()], db: PgSqlDep, request: Request):
    actions = await db.permissions.get_all_actions(q_params.limit, q_params.offset)
    return {'actions': actions}


@router.post('/create')
@require_permission(Services.access_matrix, Actions.create)
async def create_action(body: CreateActionSchema, db: PgSqlDep, request: Request):
    action_id = await db.permissions.create_action(body.name, body.description)

    if not action_id:
        raise HTTPException(status_code=409, detail='Действие с таким именем уже существует')

    return {'success': True,'message': f'Действие "{body.name}" создано','action_id': action_id}


@router.put('/{action_id}')
@require_permission(Services.access_matrix, Actions.update)
async def update_action(action_id: int, body: UpdateActionSchema, db: PgSqlDep, request: Request):
    updated = await db.permissions.update_action(action_id, body.name, body.description)

    if not updated:
        raise HTTPException(status_code=404, detail='Действие не найдено')

    return {'success': True,'message': f'Действие {action_id} обновлено'}


@router.delete('/{action_id}')
@require_permission(Services.access_matrix, Actions.delete)
async def delete_action(action_id: int, db: PgSqlDep, request: Request):
    deleted = await db.permissions.delete_action(action_id)

    if not deleted:
        raise HTTPException(status_code=404, detail='Действие не найдено')

    return {'success': True,'message': f'Действие {action_id} удалено'}
