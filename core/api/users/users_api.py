from fastapi import APIRouter, Response, Request, HTTPException

from core.api.users.rate_limiter import rate_limit
from core.data.postgres import PgSqlDep
from core.schemas.cookie_settings_schema import JWTCookieDep
from core.utils.anything import hide_log_param
from core.utils.jwt_factory import issue_aT_rT
from core.schemas.users_schema import UserRegSchema, UserLogInSchema, TokenPayloadSchema
from core.config_dir.config import encryption
from core.utils.logger import log_event

router = APIRouter(tags=['Пользователи'])



@router.post('/public/users/sign_up', summary="Регистрация")
async def registration_user(creds: UserRegSchema, db: PgSqlDep, request: Request):
    insert_attempt = await db.users.reg_user(creds.email, creds.passw, creds.first_name, creds.surname, creds.last_name, creds.role)

    if not insert_attempt:
        log_event(f"Пользователь с email: {hide_log_param(creds.email)} Уже существует", request=request, level='WARNING')
        raise HTTPException(status_code=409, detail='Пользователь уже существует')

    log_event(f"Новый пользователь! email: {hide_log_param(creds.email)}", request=request)
    return {'success': True, 'message': 'Пользователь добавлен'}



@router.post('/public/users/login', summary="Вход в аккаунт")
@rate_limit(5, 300) # для защиты от брутфорса паролей
async def log_in(creds: UserLogInSchema, response: Response, db: PgSqlDep, request: Request):
    db_user = await db.users.select_user(creds.email)

    if db_user and encryption.verify(creds.passw, db_user['passw']):
        token_schema = TokenPayloadSchema(
            id=db_user['id'],
            user_agent=request.headers.get('user-agent'),
            ip=request.state.client_ip,
            role=db_user['role'],
        )
        access_token, refresh_token = await issue_aT_rT(db,token_schema)

        response.set_cookie('access_token', access_token, httponly=True)
        response.set_cookie('refresh_token', refresh_token, httponly=True)
        log_event("Пользователь Вошёл в акк | user_id: %s", db_user['id'], request=request, level='INFO')
        return {'success': True, 'message': 'Куки у Юзера'}

    log_event(f"Пользователь с email: {hide_log_param(creds.email)} Не смог войти", request=request, level='WARNING')
    raise HTTPException(status_code=401, detail='Неверный логин или пароль')


@router.put('/private/users/logout')
async def log_out(request: Request, response: Response, db: PgSqlDep, _: JWTCookieDep):
    await db.auth.session_termination(request.state.user_id, request.state.session_id)
    response.delete_cookie('access_token')
    response.delete_cookie('refresh_token')
    log_event(f"Пользователь разлогинился | user_id: {request.state.user_id};", request=request)
    return {'success': True, 'message': 'Пользователь вне аккаунта'}


@router.put('/private/users/del_account')
async def log_out(request: Request, response: Response, db: PgSqlDep, _: JWTCookieDep):
    await db.auth.delete_account(request.state.user_id)
    response.delete_cookie('access_token')
    response.delete_cookie('refresh_token')
    log_event(f"Пользователь удалил аккаунт. Все сессии очищены | user_id: {request.state.user_id}", request=request, level='WARNING')
    return {'success': True, 'message': 'Пользователь вне аккаунта'}