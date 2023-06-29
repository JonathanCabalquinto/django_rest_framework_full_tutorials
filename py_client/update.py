import requests

data = {
    "title": "Hoi Pinoy ako HAHAH",
    "price": 129.99,
    "content": "Hindi ka Pinoy"
}
endpoint = "http://127.0.0.1:8000/api/products/11/update/"
get_response = requests.put(endpoint, json=data)
print(get_response.json())
