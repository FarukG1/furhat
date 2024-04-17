import requests

url = "http://localhost:54321/furhat"  # Replace with your desired URL

response = requests.get(url)

print(response.text)
