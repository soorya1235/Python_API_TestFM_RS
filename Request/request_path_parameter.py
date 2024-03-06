import requests

# Define the base URL with path parameter
base_url = 'https://jsonplaceholder.typicode.com/posts/{post_id}'

# Define the path parameter value
post_id = 1

# Replace the path parameter placeholder with the actual value
url = base_url.format(post_id=post_id)

# Make a GET request with the constructed URL
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Print the response content
    print("Response:")
    print(response.json())
else:
    # Print an error message if the request was not successful
    print("Error:", response.status_code)
