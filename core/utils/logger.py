import os
import inspect

import logging
from logging.config import dictConfig

from typing import Literal, Any

from starlette.requests import Request

from core.utils.anything import get_client_ip

lvls = {
    "DEBUG": 10,
    "INFO": 20,
    "WARNING": 30,
    "ERROR": 40,
    "CRITICAL": 50
}

logger_settings = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "default": {
            "()": "colorlog.ColoredFormatter",
            "format": "%(log_color)s%(levelname)-8s%(reset)s | "
                      "\033[32mD%(asctime)s\033[0m | "
                      "\033[34m%(method)s\033[0m \033[36m%(url)s\033[0m | "
                      "%(cyan)s%(location)s:%(reset)s def %(cyan)s%(func)s%(reset)s(): line - %(cyan)s%(line)d%(reset)s - \033[34m%(ip)s\033[0m "
                      "%(message)s",
            "datefmt": "%d-%m-%Y T%H:%M:%S",
            "log_colors": {
                "DEBUG": "white",
                "INFO": "green",
                "WARNING": "yellow",
                "ERROR": "red",
                "CRITICAL": "bold_red"
            }
        }
    },
    "filters": {},
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "formatter": "default",
            "level": "DEBUG"
        }
    },
    "loggers": {
        "prod_log": {
            "handlers": ["console"],
            "level": "DEBUG",
            "propagate": False
        }
    }
}

dictConfig(logger_settings)
logger = logging.getLogger('prod_log')


def log_event(event: Any, *args, request: Request = None,
              level: Literal['DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL'] = 'INFO'):
    event = str(event)
    cur_call = inspect.currentframe()
    outer = inspect.getouterframes(cur_call)[1]
    filename = os.path.relpath(outer.filename)
    func = outer.function
    line = outer.lineno

    meth, url, ip = '', '', ''
    if isinstance(request, Request):
        meth, url = request.method, str(request.url.path)
        ip = request.state.client_ip if hasattr(request.state, 'client_ip') else get_client_ip(request)


    message = event % args if args else event

    logger.log(lvls[level], message, extra={
        'method': meth,
        'location': filename,
        'func': func,
        'line': line,
        'url': url,
        'ip': ip,
    })