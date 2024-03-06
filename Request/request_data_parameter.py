import requests

# URL to which the POST request will be sent
url = 'https://httpbin.org/post'

# Form data to be sent in the request
form_data = {
    'username': 'john_doe',
    'password': 'secretpassword123'
}

# Sending a POST request with form data using the 'data' parameter
response = requests.post(url, data=form_data)

# Printing the response
print(response.text)
print("************************")
print(response.json())
