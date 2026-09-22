"""
Модуль схем Pydantic для управления пользователями.
Содержит модели для валидации данных при регистрации, хранения информации о пользователе
и формирования ответов API с автоматической поддержкой преобразования camelCase.
"""

from pydantic import BaseModel, EmailStr, ConfigDict
from pydantic.alias_generators import to_camel

class UserBaseSchema(BaseModel):
    """
    Базовая схема пользователя, содержащая общие поля (почта и ФИО).

    Настроена на автоматическую генерацию псевдонимов (alias_generator=to_camel)
    для совместимости с JSON-форматом (camelCase) и валидацию по внутренним
    именам python-стиля (validate_by_name=True).
    """
    model_config = ConfigDict(alias_generator=to_camel, validate_by_name=True)

    email: EmailStr
    last_name: str
    first_name: str
    middle_name: str

class UserSchema(UserBaseSchema):
    """
    Модель пользователя в системе.

    Наследует все базовые поля из UserBaseSchema и добавляет
    уникальный идентификатор (id), генерируемый сервером/базой данных.
    """
    id: str

class CreateUserRequestSchema(UserBaseSchema):
    """
    Схема входящего запроса на создание пользователя.

    Наследует базовые поля из UserBaseSchema и дополняет их
    обязательным полем пароля (password).
    """
    password: str

class CreateUserResponseSchema(BaseModel):
    """
    Схема успешного ответа API при создании пользователя.

    Оборачивает полную модель пользователя (UserSchema) в стандартный
    контейнер ответа сервера.
    """
    user: UserSchema