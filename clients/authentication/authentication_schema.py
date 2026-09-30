from pydantic import BaseModel, ConfigDict, Field
from pydantic.alias_generators import to_camel

from tools.fakers import fake


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
    email: str = Field(default_factory=fake.email)    # для негативных сценариев!
    password: str = Field(default_factory=fake.password)    # для положительных - явно указать при инициализации


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
    refresh_token: str = Field(default_factory=fake.sentence)     # для негативных сценариев
                                                                  # # для положительных - явно указать при инициализации