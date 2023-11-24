from os import environ

from dotenv import load_dotenv
from flask import Flask

load_dotenv()

app = Flask(__name__)


@app.get("/")
def hello_world():
    return "<p>Hello, World!</p>"


if __name__ == "__main__":
    isDebugTurnedOn = environ.get("DEBUG", False)
    app.run(debug=isDebugTurnedOn)
