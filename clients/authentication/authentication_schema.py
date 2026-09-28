from pydantic import BaseModel, ConfigDict
from pydantic.alias_generators import to_camel


class TokenSchema(BaseModel):
    """
    Описание аутентификационных токенов
    """
    model_config = ConfigDict(alias_generator=to_camel, validate_by_name=True)

    token_type: str
    access_token: str
    refresh_token: str

class LoginRequestSchema(BaseModel):
    """
    Описание структуры запроса на аутентификацию.
    """
    email: str
    password: str


class LoginResponseSchema(BaseModel):  # Добавили структуру ответа аутентификации
    """
    Описание структуры ответа аутентификации.
    """
    token: TokenSchema


class RefreshRequestSchema(BaseModel):
    model_config = ConfigDict(alias_generator=to_camel, validate_by_name=True, serialize_by_alias=True)
    """
    Описание структуры запроса для обновления токена.
    """
    refresh_token: str