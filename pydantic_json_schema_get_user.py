from clients.private_http_builder import AuthenticationUserSchema
from clients.users.private_users_client import get_private_users_client
from clients.users.public_users_client import get_public_users_client
from clients.users.users_schema import CreateUserRequestSchema, GetUserResponseSchema
from tools.assertions.schema import validate_json_schema
from tools.fakers import fake

# Инициализируем клиент PublicUsersClient
public_users_client = get_public_users_client()

# Инициализируем запрос на создание пользователя
create_user_request = CreateUserRequestSchema(
    email=fake.email(),
    password="string",
    last_name="string",
    first_name="string",
    middle_name="string"
)

create_user_response = public_users_client.create_user_api(create_user_request)
create_user_response_json = create_user_response.json()

# Инициализируем пользовательские данные для аутентификации
authentication_user = AuthenticationUserSchema(
    email=create_user_request.email,
    password=create_user_request.password
)
# Инициализируем клиент PrivateUsersClient
private_users_client = get_private_users_client(authentication_user)
get_user_response = private_users_client.get_user_api(create_user_response_json["user"]["id"])
get_user_response_json = get_user_response.json()

# Генерируем JSON schema из модели GetUserResponseSchema
get_user_response_schema = GetUserResponseSchema.model_json_schema()

# Валидируем ответ по JSON schema
validate_json_schema(instance=get_user_response_json, schema=get_user_response_schema)
