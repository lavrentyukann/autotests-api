import httpx
from tools.fakers import get_random_email  # Импортируем функцию для генерации случайного email

client = httpx.Client(base_url="http://localhost:8000/api/v1")
# Создаем пользователя
create_user_payload = {
    "email": get_random_email(),  # Используем функцию для генерации случайного email
    "password": "string",
    "lastName": "string",
    "firstName": "string",
    "middleName": "string"
}
create_user_response = client.post("/users", json=create_user_payload)
create_user_response_data = create_user_response.json()
print('Create user data :', create_user_response_data)

# Проходим аутентификацию и добавляем токен в клиент
login_payload = {
    "email": create_user_payload["email"],
    "password": create_user_payload["password"]
}
login_response = client.post("/authentication/login", json=login_payload)
login_data = login_response.json()
print('Login data :', login_data)

client.headers["authorization"] = f"Bearer {login_data['token']['accessToken']}"

# Запрос на обновление пользователя
update_user_headers = {
    "Authorization": login_data['token']['accessToken']
}
update_user_payload = {
  "email": get_random_email(),
  "lastName": "string",
  "firstName": "string",
  "middleName": "string"
}
update_user_response = client.patch(f"/users/{create_user_response_data['user']['id']}", json=update_user_payload)
print('Update user status code:', update_user_response.status_code)
update_user_response_data = update_user_response.json()
print('Update user data:', update_user_response_data)