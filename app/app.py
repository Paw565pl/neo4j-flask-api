from os import environ

from dotenv import load_dotenv
from flask import Flask
from neomodel import config

from app.commands import seed_db
from app.routes.departments import departments_blueprint
from app.routes.employees import employees_blueprint

load_dotenv()
config.DATABASE_URL = environ.get("NEO4J_BOLT_URL")

app = Flask(__name__)

app.register_blueprint(employees_blueprint, url_prefix="/employees")
app.register_blueprint(departments_blueprint, url_prefix="/departments")

app.cli.add_command(seed_db)
