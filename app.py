from os import environ

from dotenv import load_dotenv
from flask import Flask
from neomodel import config

load_dotenv()

app = Flask(__name__)


@app.get("/")
def hello_world():
    return "<p>Hello, World!</p>"


if __name__ == "__main__":
    config.DATABASE_URL = environ.get("NEO4J_BOLT_URL")

    isDebugTurnedOn = bool(environ.get("DEBUG", False))
    app.run(debug=isDebugTurnedOn)
