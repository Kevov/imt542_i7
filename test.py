import requests

print(requests.get('https://d113-76-22-92-25.ngrok-free.app/').text)

print(requests.get('https://d113-76-22-92-25.ngrok-free.app/gamelist').json())