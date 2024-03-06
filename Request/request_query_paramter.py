import requests

# Define the base URL
base_url = 'https://jsonplaceholder.typicode.com/posts'

# Define the query parameters as a dictionary
query_params = {
    'userId': 1  # Filter posts by user ID 1
}

# Make a GET request with query parameters
response = requests.get(base_url, params=query_params)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Print the response content (list of posts)
    print("Response:")
    print(response.json())
else:
    # Print an error message if the request was not successful
    print("Error:", response.status_code)
