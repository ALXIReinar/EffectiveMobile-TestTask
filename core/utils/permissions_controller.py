from functools import wraps
from fastapi import HTTPException
from starlette.requests import Request
from core.data.postgres import PgSql
from core.utils.logger import log_event


def require_permission(service: str, action: str):
    """
    Требует Request в эндпоинте!
    Чувствителен к Request объекту. Рекомендуется указывать в эндпоинте "request: Request"
    """
    def decorator(func):
        @wraps(func)
        async def wrapper(*args, **kwargs):
            """"""
            "Получаем 'request'"
            log_event(f'{args}\n\n{kwargs}', level="DEBUG")
            request: Request = kwargs.get('request') or next((arg for arg in args if isinstance(arg, Request)), None)

            if not request:
                raise HTTPException(status_code=500, detail="Internal error: missing request or db")
            
            role = request.state.role
            
            if role is None:
                raise HTTPException(status_code=401, detail="Требуется авторизация")
            
            "Проверка прав"
            async with request.app.state.pg_pool.acquire() as conn:
                db = PgSql(conn)
                has_permission = await db.permissions.check_permission(role, service, action)
            
            if not has_permission:
                raise HTTPException(
                    status_code=403, 
                    detail=f"Недостаточно прав для взаимодействия с ресурсом. {service}:{action}"
                )
            
            return await func(*args, **kwargs)
        
        return wrapper
    return decorator
