import httpx

client = httpx.Client(base_url="http://localhost:8000")

payload = {
    "email": "userka@example.com",
    "password": "string"
}

login_response = client.post("http://localhost:8000/api/v1/authentication/login", json=payload)
login_response_data = login_response.json()
print("Status Code: ", login_response.status_code)
print("Login response: ", login_response_data)

access_token = login_response_data["token"]["accessToken"]
print("Access Token: ", access_token)

client.headers["Authorization"] =  f"Bearer {access_token}"
me_response = client.get("http://localhost:8000/api/v1/users/me")
print("Status Code: ", me_response.status_code)
print(me_response.json())

client.close()