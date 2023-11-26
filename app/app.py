from os import environ

from dotenv import load_dotenv
from flask import Flask
from neomodel import config

from routes.departments import departments_blue_print
from routes.employees import employees_blue_print
from routes.seed import seed_blueprint

load_dotenv()
config.DATABASE_URL = environ.get("NEO4J_BOLT_URL")

app = Flask(__name__)

app.register_blueprint(seed_blueprint, url_prefix="/seed")
app.register_blueprint(employees_blue_print, url_prefix="/employees")
app.register_blueprint(departments_blue_print, url_prefix="/departments")

if __name__ == "__main__":
    isDebugTurnedOn = True if environ.get("DEBUG") == "True" else False
    app.run(debug=isDebugTurnedOn)
