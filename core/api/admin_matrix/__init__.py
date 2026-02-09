from fastapi import APIRouter
from .actions_api import router as actions_router
from .services_api import router as services_router
from .permissions_api import router as permissions_router
from .roles_api import router as roles_router

admin_matrix_router = APIRouter(prefix='/admin', tags=['Admin - Матрица доступа'])

admin_matrix_router.include_router(actions_router)
admin_matrix_router.include_router(services_router)
admin_matrix_router.include_router(permissions_router)
admin_matrix_router.include_router(roles_router)
