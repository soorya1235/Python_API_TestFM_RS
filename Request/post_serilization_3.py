import requests

"""
If you want to test serialization and deserialization using JSON with Python requests, 
you can use the JSONPlaceholder API to send and receive JSON data.
"""

import requests

# Sample URL
url = 'https://jsonplaceholder.typicode.com/posts'

# Sample data to be serialized (Python dictionary)
data = {'title': 'Test Post', 'body': 'This is a test post.', 'userId': 1}

# Make a POST request with JSON data
response = requests.post(url, json=data)

# Deserialize JSON response into Python object
response_data = response.json()

# Print the response data
print(response_data)
