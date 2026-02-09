from functools import wraps
from fastapi import HTTPException
from starlette.requests import Request
from core.data.postgres import PgSql


def require_permission(service_id: int, action_id: int):
    """
    Декоратор для проверки прав доступа (использует ID для максимальной производительности)
    
    Требует Request в эндпоинте!
    Чувствителен к Request объекту. Рекомендуется указывать в эндпоинте "request: Request"
    
    Использование:
    @require_permission(Services.analytics, Actions.read)
    async def get_metrics(request: Request):
        ...
    """
    def decorator(func):
        @wraps(func)
        async def wrapper(*args, **kwargs):
            """"""
            "Получаем 'request'"
            request: Request = kwargs.get('request') or next((arg for arg in args if isinstance(arg, Request)), None)

            if not request:
                raise HTTPException(status_code=500, detail="Internal error: missing request")
            
            role = request.state.role
            
            if role is None:
                raise HTTPException(status_code=401, detail="Требуется авторизация")
            
            "Проверка прав"
            async with request.app.state.pg_pool.acquire() as conn:
                db = PgSql(conn)
                has_permission = await db.permissions.check_permission(role, service_id, action_id)
            
            if not has_permission:
                raise HTTPException(
                    status_code=403, 
                    detail=f"Недостаточно прав для взаимодействия с ресурсом"
                )
            
            return await func(*args, **kwargs)
        
        return wrapper
    return decorator
