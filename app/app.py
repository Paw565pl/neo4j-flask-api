from os import environ

from dotenv import load_dotenv
from flask import Flask
from neomodel import config
from routes.seed import seed_db

load_dotenv()
config.DATABASE_URL = environ.get("NEO4J_BOLT_URL")

app = Flask(__name__)
app.add_url_rule("/seed", view_func=seed_db, methods=["POST"])


if __name__ == "__main__":
    isDebugTurnedOn = bool(environ.get("DEBUG", False))
    app.run(debug=isDebugTurnedOn)
