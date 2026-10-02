from clients.authentication.authentication_client import get_authentication_client
from clients.users.public_users_client import get_public_users_client
from clients.users.users_schema import CreateUserRequestSchema
from clients.authentication.authentication_schema import LoginRequestSchema, LoginResponseSchema
from http import HTTPStatus
from tools.assertions.base import assert_status_code
from tools.assertions.schema import validate_json_schema
from tools.assertions.authentication import assert_login_response


def test_login():
    # Инициализируем API-клиент для работы с пользователями
    public_users_client = get_public_users_client()
    authentication_client = get_authentication_client()

    # Формируем тело запроса на создание пользователя
    request_create_user = CreateUserRequestSchema()

    # Отправляем запрос на создание пользователя
    public_users_client.create_user(request_create_user)

    # Формируем тело запроса на аутентификацию
    request_login_user = LoginRequestSchema()

    # Перезаписываем логин и пароль из созданного ранее пользователя (т.к. в LoginRequestSchema по умолчанию fake-данные)
    request_login_user.email = request_create_user.email
    request_login_user.password = request_create_user.password

    # Отправляем запрос на аутентификацию
    response_login_user = authentication_client.login_api(request_login_user)

    # Инициализируем модель ответа на основе полученного JSON в ответе
    # Также благодаря встроенной валидации в Pydantic дополнительно убеждаемся, что ответ корректный
    response_data_login_user = LoginResponseSchema.model_validate_json(response_login_user.text)

    # Проверяем статус-код ответа
    assert_status_code(response_login_user.status_code, HTTPStatus.OK)

    # Проверяем, что данные ответа совпадают с данными запроса
    assert_login_response(response_data_login_user)

    validate_json_schema(response_login_user.json(), response_data_login_user.model_json_schema())