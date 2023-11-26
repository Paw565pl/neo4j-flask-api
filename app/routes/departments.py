from flask import jsonify, request, Blueprint
from models import Department

departments_blue_print = Blueprint("department", __name__)


@departments_blue_print.get("/")
async def get_departments():
    name = request.args.get("name", "")
    order_by = request.args.get("order_by")

    try:
        departments = Department.nodes.filter(name__istartswith=name).order_by(order_by)
        data = [department.get_json() for department in departments]

        return jsonify(data)

    except Exception as e:
        return jsonify({"error_type": type(e).__name__, "message": str(e)}), 400


@departments_blue_print.get("/<uuid>")
async def get_department(uuid):
    try:
        department = Department.nodes.get(uuid=uuid)
        data = department.get_json()

        return jsonify(data)

    except Exception as e:
        return jsonify({"error_type": type(e).__name__, "message": str(e)}), 400


@departments_blue_print.get("/<uuid>/employees")
async def get_department_employees(uuid):
    try:
        department_employees = Department.nodes.get(uuid=uuid).works_in.all()
        data = [employee.get_json() for employee in department_employees]

        return jsonify(data)

    except Exception as e:
        return jsonify({"error_type": type(e).__name__, "message": str(e)}), 400
