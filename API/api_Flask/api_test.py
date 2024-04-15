import requests

url="http://127.0.0.1:5000/login"
params={
    'email':'dpshah2307@gmail.com',
    'password':'hello123'
}

response = requests.post(url, data=params)
if response.status_code == 200:
    # Request was successful
    print("Authentication successful")
    print(response.json())  # Print the response data
else:
    # Request failed
    print("Failed to authenticate:", response.status_code)