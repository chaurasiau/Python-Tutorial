import requests

response = requests.get('https://www.python.org/')
print(f"Response Code - {response.status_code}")
