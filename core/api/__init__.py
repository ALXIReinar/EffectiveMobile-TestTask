from fastapi import APIRouter
from .users.users_api import router as users_router
from .admin_matrix import admin_matrix_router
from core.api.services import service_router

main_router = APIRouter(prefix='/api/v1')

main_router.include_router(users_router)
main_router.include_router(admin_matrix_router)
main_router.include_router(service_router)


@main_router.get('/public/healthcheck')
def healthcheck():
    return {'status': True, 'message': 'Auth Service'}