import requests

endpoint = "http://127.0.0.1:8000/api/"

# get_response = requests.get(
#     endpoint, params={"product_id": 123}, json={"product_id": 123})
post_response = requests.post(
    endpoint, params={"product_id": 123}, json={"title": "Abc123", "content": "Hello world"})
print(post_response.json())
