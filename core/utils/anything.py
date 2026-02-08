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
    admin = 'admin'
    project_manager = 'project_manager'
    data_analyst = 'data_analyst'
    security = 'security'
    developer = 'developer'
    hr = 'hr'



def hide_log_param(param, start=3, end=8):
    return param[:start] + '*' * len(param[start:-end-1]) + param[-end:]

def get_client_ip(request: Request):
    xff = request.headers.get('X-Forwarded-For')
    ip = xff.split(',')[0].strip() if (
            xff and request.client.host in env.trusted_proxies
    ) else request.client.host
    return ip