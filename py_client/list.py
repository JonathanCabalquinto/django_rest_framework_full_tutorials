import requests
from getpass import getpass
auth_endpoint = "http://127.0.0.1:8000/api/auth/"
password = getpass()
data_s = {
    "username": 'staff',
    "password": password
}
auth_response = requests.post(auth_endpoint, json=data_s)
print(auth_response.json())


if (auth_response.status_code == 200):
    token = auth_response.json()['token']
    headers = {
        "Authorization": f"Bearer {token}"
    }
    print(headers)
    endpoint = "http://127.0.0.1:8000/api/products/"
    get_response = requests.get(endpoint, headers=headers)
    print(get_response.json())
