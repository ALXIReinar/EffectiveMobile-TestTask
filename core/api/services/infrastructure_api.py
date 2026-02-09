from fastapi import APIRouter
from starlette.requests import Request

from core.schemas.cookie_settings_schema import JWTCookieDep
from core.utils.anything import Services, Actions
from core.utils.permissions_controller import require_permission

router = APIRouter(prefix='/infrastructure', tags=['Infrastructure'], dependencies=[JWTCookieDep])


@router.get('/servers')
@require_permission(Services.infrastructure, Actions.read)
async def get_servers(request: Request):
    """Просмотр серверов (доступно: admin, devops, developer, project_manager, security)"""
    return {
        'servers': [
            {'id': 1, 'name': 'prod-web-01', 'status': 'running', 'cpu': '45%'},
            {'id': 2, 'name': 'prod-api-01', 'status': 'running', 'cpu': '62%'},
            {'id': 3, 'name': 'prod-db-01', 'status': 'running', 'cpu': '78%'}
        ]
    }


@router.post('/deploy')
@require_permission(Services.infrastructure, Actions.deploy)
async def deploy_app(request: Request):
    """Деплой приложения (доступно: admin, devops, developer)"""
    return {'success': True, 'message': 'Деплой начался', 'build_id': 'build-12345'}


@router.delete('/servers/{server_id}')
@require_permission(Services.infrastructure, Actions.manage)
async def delete_server(server_id: int, request: Request):
    """Удаление сервера (доступно: admin, devops)"""
    return {'success': True, 'message': f'Сервер {server_id} удалён'}
