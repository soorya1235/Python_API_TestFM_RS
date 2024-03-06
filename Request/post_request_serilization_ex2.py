import requests
import json

# Sample URL
url = 'https://jsonplaceholder.typicode.com/posts'

# Sample data to be serialized
data = {'title': 'Test Post', 'body': 'This is a test post.', 'userId': 1}

headers={'Content-Type': 'application/json'}
response = requests.post(url, data=data)
print(type(data))
print(response.json())


#Serialize the data in to string
json_data = json.dumps(data)
print(type(json_data))
print(json_data)

# Make a POST request with serialized JSON data
response = requests.post(url, data=json_data, headers={'Content-Type': 'application/json'})

# Deserialize JSON data received in the response
response_data = response.json()

# Print the deserialized response data
print(response_data)
