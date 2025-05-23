from flask import Flask
import requests
import json

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/gamelist")
def game_list():
    url = 'https://store.steampowered.com/api/appdetails?appids=10'
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Get Games Detail Failed failed: {response.status_code} - {response.text}")
    
@app.route("/whatisthis")
def what_is_this():
    return "<h1> This is a test</h1>"