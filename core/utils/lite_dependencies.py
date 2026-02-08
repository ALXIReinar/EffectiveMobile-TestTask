from typing import Annotated

from fastapi import HTTPException, Depends
from pydantic import BaseModel, Field
from starlette.requests import Request

class Pagination(BaseModel):
    limit: int = Field(10, ge=1)
    offset: int = Field(0, ge=0)

PagenDep = Annotated[Pagination, Depends(Pagination)]

def role_require(*roles: str):
    async def checker(request: Request):
        cur_role = request.state.role

        "Проверка на соответствие указанным ролям"
        if cur_role not in set(roles):
            raise HTTPException(status_code=403, detail="Недостаточно прав")

    return checker