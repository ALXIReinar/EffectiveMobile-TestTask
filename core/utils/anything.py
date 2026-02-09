from starlette.requests import Request

from core.config_dir.config import env


from dataclasses import dataclass


@dataclass
class TokenTypes:
    access_token: str = 'aT'
    refresh_token: str = 'rT'

token_types = {
    'access_token': 'aT',
    'refresh_token': 'rT',
}

@dataclass
class Roles:
    admin: int = 1
    devops: int = 2
    developer: int = 3
    project_manager: int = 4
    data_analyst: int = 5
    finance_manager: int = 6
    hr: int = 7
    security: int = 8


@dataclass
class Services:
    """id таблицы services"""
    users: int = 1
    analytics: int = 2
    infrastructure: int = 3
    finance: int = 4
    access_matrix: int = 5


@dataclass
class Actions:
    """id таблицы actions"""
    read: int = 1
    write: int = 2
    create: int = 3
    update: int = 4
    delete: int = 5
    deploy: int = 6
    manage: int = 7
    read_salaries: int = 8
    read_security: int = 9



def hide_log_param(param, start=3, end=8):
    return param[:start] + '*' * len(param[start:-end-1]) + param[-end:]

def get_client_ip(request: Request):
    xff = request.headers.get('X-Forwarded-For')
    ip = xff.split(',')[0].strip() if (
            xff and request.client.host in env.trusted_proxies
    ) else request.client.host
    return ip