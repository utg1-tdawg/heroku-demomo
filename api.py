import os
import urllib.parse
from flask import Flask
from flask_cors import CORS
from pymongo import MongoClient


app = Flask(__name__, static_folder="client/build", static_url_path="/")
CORS(
    app,
    resources={
        r"/*": {
            "origins": ["http://localhost:3000", "https://heroku-demomo.herokuapp.com/"]
        }
    },
)

mongo_uri = (
    "mongodb+srv://wt:"
    + urllib.parse.quote_plus(os.environ.get("FLASK_DB_PW"))
    + "@cluster0.pctkw.mongodb.net/?retryWrites=true&w=majority"
)
client = MongoClient(mongo_uri)
db = client.nba
Players = db.players


@app.route("/")
def index():
    return app.send_static_file("index.html")


@app.route("/api")
def api():
    return {
        "env": os.environ.get("FLASK_DEMOMO_VAR"),
        "db": Players.find_one({"name": "Stephen CUrry"}).get("name"),
    }
