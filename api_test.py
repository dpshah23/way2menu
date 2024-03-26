import requests

url = "http://127.0.0.1:8000/login/"
payload = {
    "email": "dpshah2307@gmail.com",
    "password": "hello123"
}

response = requests.post(url, data=payload)

if response.status_code == 200:
    print("Request successful")
    print(response.json())
else:
    print("Error:", response.status_code)
