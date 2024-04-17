import json
import requests

# Test Connection
response = requests.get("http://localhost:54321/furhat")
print(response.text)

# Get all gestures
response = requests.get("http://localhost:54321/furhat/gestures")
print(json.dumps(response.json(), indent=4))

# Say something
data = {
    "text": "Test Hallo",
    "url": "",
    "blocking": False,
    "lipsync": False,
    "abort": False
}
response = requests.post("http://localhost:54321/furhat/say", json=data)
print(json.dumps(response.json(), indent=4))
