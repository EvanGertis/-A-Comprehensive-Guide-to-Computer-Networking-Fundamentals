import requests

# Define the URL to request
url = "https://www.google.com/"

# Make the request and get the response
response = requests.get(url)

# Print the response status code
print("Response status code:", response.status_code)

# Print the response headers
print("Response headers:")
for header, value in response.headers.items():
    print(f"{header}: {value}")

# Print the response content
print("Response content:")
print(response.content)