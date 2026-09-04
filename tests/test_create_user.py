import httpx
from clients.users.public_users_client import PublicUsersClient

client = PublicUsersClient(
    client=httpx.Client(base_url="http://localhost:8000")
)

response = client.create_user_api({
    "email": "userT@gmail.com",
    "password": "123456",
    "lastName": "string",
    "firstName": "string",
    "middleName": "string"
})

print(response.status_code)
print(response.json())
