from fastapi import APIRouter
from .analytics_api import router as analytics_router
from .infrastructure_api import router as infrastructure_router
from .finance_api import router as finance_router

service_router = APIRouter(prefix="/private")


service_router.include_router(analytics_router)
service_router.include_router(infrastructure_router)
service_router.include_router(finance_router)