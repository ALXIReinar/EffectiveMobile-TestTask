from contextlib import asynccontextmanager

import uvicorn
from asyncpg import create_pool
from fastapi import FastAPI
from redis.asyncio import Redis
from starlette.middleware.cors import CORSMiddleware

from core.api import main_router
from core.api.middleware import AuthUXASGIMiddleware
from core.config_dir.config import pool_settings, env, redis_settings


@asynccontextmanager
async def lifespan(web_app):
    """"""
    "Соединение с БД"
    web_app.state.pg_pool = await create_pool(**pool_settings)
    "Соединение с Редисом"
    web_app.state.redis = Redis(**redis_settings, decode_responses=True)

    try:
        yield
    finally:
        await web_app.state.pg_pool.close()
        await web_app.state.redis.close()

app = FastAPI(lifespan=lifespan, openapi_url="/api/v1/public/openapi.json", docs_url="/api/v1/public/docs")
app.include_router(main_router)


"Миддлвари"
app.add_middleware(
    CORSMiddleware, # Без неё фронт-часть не сможет отобразить данные
    allow_origins=["http://localhost", "http://127.0.0.1", "http://localhost:8000", "http://127.0.0.1:8000"],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*']
)
app.add_middleware(AuthUXASGIMiddleware) # авторизация


if __name__ == '__main__':
    uvicorn.run(
        'core.main:app',
        host="0.0.0.0",
        port=8000,
        workers=env.uvi_workers # изменить при большом количестве запросов для повышения производительности
    )