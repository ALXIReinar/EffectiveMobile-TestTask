from fastapi import APIRouter, Depends

from core.data.postgres import PgSqlDep
from core.utils.anything import Roles
from core.utils.lite_dependencies import role_require


router = APIRouter(
    prefix='/admin',
    tags=['Admin'],
    dependencies=[Depends(role_require(Roles.admin))]
)


@router.get('/all_services')
async def all_services(db: PgSqlDep):
    services = await db.admin.all_services()
    return services