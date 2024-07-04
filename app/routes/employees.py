from flask import jsonify, request, Blueprint
from neomodel import db, DoesNotExist

from app.models import Department, Employee

employees_blueprint = Blueprint("employees", __name__)


@employees_blueprint.get("/")
async def get_employees():
    first_name = request.args.get("first_name", "")
    last_name = request.args.get("last_name", "")
    position = request.args.get("position", "").lower()
    order_by = request.args.get("order_by")

    employees = Employee.nodes.filter(
        first_name__istartswith=first_name, last_name__istartswith=last_name
    ).order_by(order_by)
    employees_filtered_by_position = [
        employee
        for employee in employees
        if employee.works_in.relationship(employee.works_in.get())
        .position.lower()
        .startswith(position)
    ]
    data = [employee.get_json() for employee in employees_filtered_by_position]

    return jsonify(data)


@employees_blueprint.post("/")
async def create_employee():
    body = request.get_json()
    properties = _validate_request_body(body)

    with db.transaction:
        new_employee = Employee()
        new_employee.first_name = properties["first_name"]
        new_employee.last_name = properties["last_name"]
        new_employee.age = properties["age"]
        new_employee.save()

        try:
            department = Department.nodes.get(name=properties["department_name"])
        except DoesNotExist:
            raise ValueError("department with given name does not exist")

        new_employee.works_in.connect(  # type: ignore
            department,
            {"position": properties["position"], "salary": properties["salary"]},
        )

    return jsonify(new_employee.get_json()), 201


@employees_blueprint.put("/<uuid>")
async def update_employee(uuid):
    employee = Employee.nodes.get(uuid=uuid)

    body = request.get_json()
    properties = _validate_request_body(body)

    with db.transaction:
        employee.first_name = properties["first_name"]
        employee.last_name = properties["last_name"]
        employee.age = properties["age"]
        employee.save()

        old_department = employee.works_in.get()
        rel = employee.works_in.relationship(old_department)

        rel.position = properties["position"]
        rel.salary = properties["salary"]
        rel.save()

        try:
            new_department = Department.nodes.get(name=properties["department_name"])
        except DoesNotExist:
            raise ValueError("department with given name does not exist")

        employee.works_in.reconnect(old_department, new_department)

    return jsonify(employee.get_json())


@employees_blueprint.delete("/<uuid>")
async def delete_employee(uuid):
    employee = Employee.nodes.get(uuid=uuid)

    if len(employee.manages) != 0:
        return (
            jsonify(
                {
                    "message": "this employee can not be deleted, because he is manager and is associated with one or more subordinates"
                }
            ),
            405,
        )

    employee.delete()
    return jsonify({"message": "employee removed successfully"})


@employees_blueprint.get("/<uuid>/subordinates")
async def get_employee_subordinates(uuid):
    manager = Employee.nodes.get(uuid=uuid)
    subordinates = manager.manages.all()
    data = [subordinate.get_json() for subordinate in subordinates]

    return jsonify(data)


def _validate_request_body(body):
    required_fields = [
        "first_name",
        "last_name",
        "age",
        "department_name",
        "position",
        "salary",
    ]
    data = {}
    errors = []

    for field in required_fields:
        param = body.get(field)
        if not param:
            errors.append(f"{field} is required")
        else:
            data[field] = param

    if len(errors) != 0:
        raise ValueError(", ".join(errors))
    return data
