from fastapi import APIRouter
from starlette.requests import Request

from core.utils.anything import Services, Actions
from core.utils.permissions_controller import require_permission

router = APIRouter(prefix='/finance', tags=['Finance'])


@router.get('/budgets')
@require_permission(Services.finance, Actions.read)
async def get_budgets(request: Request):
    """Просмотр бюджетов (доступно: admin, project_manager, finance_manager)"""
    return {
        'budgets': [
            {'department': 'Engineering', 'allocated': 500000, 'spent': 342000},
            {'department': 'Marketing', 'allocated': 200000, 'spent': 156000}
        ]
    }


@router.post('/expenses')
@require_permission(Services.finance, Actions.write)
async def create_expense(request: Request):
    """Создать расход (доступно: admin, finance_manager)"""
    return {'success': True, 'message': 'Расход зафиксирован'}


@router.get('/salaries')
@require_permission(Services.finance, Actions.read)
async def get_salaries(request: Request):
    """Просмотр зарплат (доступно: admin, finance_manager, hr)"""
    return {
        'salaries': ['salary1', 'salary2', 'salary3'],
        'count': 150
    }