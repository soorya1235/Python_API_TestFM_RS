import requests
import json

# Sample URL
url = 'https://jsonplaceholder.typicode.com/posts'

# Sample data to be serialized
data = {'title': 'Test Post', 'body': 'This is a test post.', 'userId': 1}

#Serialize the data into JSON format
json_data = json.dumps(data)
print(type(json_data))



# Make a POST request with serialized JSON data
response = requests.post(url, data=json_data, headers={'Content-Type': 'application/json'})

# Deserialize JSON data received in the response
response_data = response.json()

# Print the deserialized response data
print(response_data)
