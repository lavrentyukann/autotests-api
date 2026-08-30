import httpx
from tools.fakers import get_random_email

# Создаем пользователя
create_user_payload = {
    "email": get_random_email(),  # Используем функцию для генерации случайного email
    "password": "string",
    "lastName": "string",
    "firstName": "string",
    "middleName": "string"
}
create_user_response = httpx.post("http://localhost:8000/api/v1/users", json=create_user_payload)
create_user_response_data = create_user_response.json()
print('Create user data :', create_user_response_data)

# Проходим авторизацию
login_payload = {
    "email": create_user_payload["email"],
    "password": create_user_payload["password"]
}
login_response = httpx.post("http://localhost:8000/api/v1/authentication/login", json=login_payload)
login_data = login_response.json()
print('Login data :', login_data)

# Инициализируем клиент с авторизацией
client = httpx.Client(
    base_url="http://localhost:8000",
    timeout=100,
    headers={"Authorization": f"Bearer {login_data['token']['accessToken']}"}
)

# Выполняем запрос с авторизацией
get_user_me_response = client.get("/api/v1/users/me")
get_user_me_response_data = get_user_me_response.json()
print('Get user me data:', get_user_me_response_data)