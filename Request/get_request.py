import requests

baseurl = "https://reqres.in"
endpoint = "/api/users"
data = {'page':2}
print(baseurl+endpoint)
response = requests.get(baseurl+endpoint,data=data)
print(response.json())
print(response.status_code)
print(response.headers)
