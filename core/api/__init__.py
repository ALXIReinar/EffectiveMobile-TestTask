from fastapi import APIRouter
from .users.users_api import router as users_router
from .admin_api import router as admin_router

main_router = APIRouter(prefix='/api/v1')

main_router.include_router(users_router)
main_router.include_router(admin_router)


@main_router.get('/public/healthcheck')
def healthcheck():
    return {'status': True, 'message': 'Auth Service'}