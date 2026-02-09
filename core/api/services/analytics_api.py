from fastapi import APIRouter
from starlette.requests import Request

from core.schemas.cookie_settings_schema import JWTCookieDep
from core.utils.anything import Services, Actions
from core.utils.permissions_controller import require_permission

router = APIRouter(prefix='/analytics', tags=['Analytics'], dependencies=[JWTCookieDep])

@router.get('/metrics')
@require_permission(Services.analytics, Actions.read)
async def get_metrics(request: Request):
    """Получить метрики (доступно: admin, devops, developer, project_manager, data_analyst)"""
    return {'data': {
        'daily_active_users': 15420,
        'conversion_rate': 3.2,
        'avg_session_duration': '8m 34s'
        }
    }


@router.post('/reports')
@require_permission(Services.analytics, Actions.write)
async def create_report(request: Request):
    """Создать отчет (доступно: admin, project_manager, data_analyst)"""
    return {'success': True, 'message': 'Отчёт создан!'}