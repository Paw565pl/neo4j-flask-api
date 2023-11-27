from flask import jsonify, request, Blueprint
from models import Department

from utils.handle_exception import handle_exception

# from utils.handle_exception import handle_exception

departments_blue_print = Blueprint("department", __name__)


@departments_blue_print.get("/")
@handle_exception
async def get_departments():
    name = request.args.get("name", "")
    order_by = request.args.get("order_by")

    departments = Department.nodes.filter(name__istartswith=name).order_by(order_by)
    data = [department.get_json() for department in departments]

    return jsonify(data)


@departments_blue_print.get("/<uuid>")
@handle_exception
async def get_department(uuid):
    department = Department.nodes.get(uuid=uuid)
    data = department.get_json()

    return jsonify(data)


@departments_blue_print.get("/<uuid>/employees")
@handle_exception
async def get_department_employees(uuid):
    department_employees = Department.nodes.get(uuid=uuid).works_in.all()
    data = [employee.get_json() for employee in department_employees]

    return jsonify(data)
