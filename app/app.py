from os import environ

from dotenv import load_dotenv
from flask import Flask
from neomodel import config
from routes.employees import (
    create_employee,
    delete_employee,
    get_employees,
    update_employee,
)
from routes.seed import seed_db

load_dotenv()
config.DATABASE_URL = environ.get("NEO4J_BOLT_URL")

app = Flask(__name__)

app.add_url_rule("/seed", view_func=seed_db, methods=["POST"])
app.add_url_rule("/employees", view_func=get_employees, methods=["GET"])
app.add_url_rule("/employees", view_func=create_employee, methods=["POST"])
app.add_url_rule("/employees/<uuid>", view_func=update_employee, methods=["PUT"])
app.add_url_rule("/employees/<uuid>", view_func=delete_employee, methods=["DELETE"])

if __name__ == "__main__":
    isDebugTurnedOn = bool(environ.get("DEBUG", False))
    app.run(debug=isDebugTurnedOn)
