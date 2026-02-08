import html
import re
import secrets

from pydantic import BaseModel, Field, field_validator
from pydantic import EmailStr
from pydantic_core.core_schema import FieldValidationInfo


class ValidatePasswSchema(BaseModel):
    confirm_password: str
    passw: str
    @field_validator('passw', check_fields=False, mode='after')
    @classmethod
    def validate_password(cls, value, info: FieldValidationInfo):
        passw = value.strip()
        if len(passw) < 8:
            raise ValueError('String shorter 8 characters')

        if len(passw.encode('utf-8')) > 72:
            raise ValueError('Password too long (max 72 bytes)')
        spec_spell = digit = uppercase = False

        for ch in passw:
            if re.match(r'[А-Яа-я]', ch):
                raise ValueError('Password must consist of English chars only')
            if ch == ' ':
                raise ValueError('Password must not contain spaces')

            if ch.isdigit():
                digit = True
            elif ch in {'.', ';', '\\', '!', '_', '/', '&', ')', '>', '$', '*', '}', '=', ',', '[', '#', '%', '~', ':',
                        '{', ']', '?', '@', "'", '(', '`', '"', '^', '|', '<', '-', '+', '№'}:
                spec_spell = True
            elif ch == ch.upper():
                uppercase = True


        "Проверка, что оба введённых пароля идентичны"
        if not secrets.compare_digest(passw, info.data['confirm_password']):
            raise ValueError('Password does not match')

        "Проверка на выолнение условий надёжности пароля"
        if spec_spell and digit and uppercase:
            return passw
        raise ValueError('Password does not match the conditions: 1 Spec char, 1 digit, 1 Uppercase letter')



class UserLogInSchema(BaseModel):
    email: EmailStr
    passw: str

class UserRegSchema(ValidatePasswSchema):
    email: EmailStr
    first_name: str
    surname: str
    last_name: str
    role: str

class RecoveryPasswSchema(BaseModel):
    email: EmailStr


class TokenPayloadSchema(BaseModel):
    id: int
    role: str
    user_agent: str = Field(max_length=200)
    ip: str = Field(max_length=45)  # IPv6 может быть до 45 символов

    @field_validator('user_agent')
    @classmethod
    def sanitize_user_agent(cls, value: str) -> str:
        # Экранируем HTML и удаляем потенциально опасные символы
        sanitized = html.escape(value)
        # Удаляем управляющие символы
        sanitized = ''.join(char for char in sanitized if ord(char) >= 32)
        return sanitized[:200]  # Обрезаем до максимума
