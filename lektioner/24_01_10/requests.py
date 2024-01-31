import requests
# The requests library in Python is a popular and easy-to-use HTTP library.
# It allows you to send HTTP/1.1 requests, without the need to manually add query strings to your URLs, or form-encode your POST data.

# Basic Usage Examples:

# GET request
response = requests.get('https://api.example.com/data')
data = response.json() # Parse JSON response

# POST request with JSON data
response = requests.post('https://api.example.com/submit', json={'key': 'value'})