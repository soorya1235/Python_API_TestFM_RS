import requests

payload = {
    "name": "morpheus",
    "job": "leader"
}
url = "https://reqres.in/api/users"
response = requests.post(url,json=payload)
print(response.status_code)
print(response.json())