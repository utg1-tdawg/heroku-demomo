import os
from flask import Flask
from flask_cors import CORS


app = Flask(__name__, static_folder="client/build", static_url_path='/')
CORS(
    app,
    resources={
        r"/*": {
            "origins": ["http://localhost:3000", "https://heroku-demomo.herokuapp.com/"]
        }
    },
)

@app.route('/')
def index():
    return app.send_static_file('index.html')

@app.route("/api")
def api():
    return {"api": os.environ.get("FLASK_DEMOMO_VAR")}
