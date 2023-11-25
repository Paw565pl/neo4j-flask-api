from flask import jsonify, request
from models import Department, Employee
from neomodel import db


async def get_employees():
    first_name = request.args.get("first_name", "")
    last_name = request.args.get("last_name", "")
    position = request.args.get("position", "")
    orderBy = request.args.get("order_by", None)

    try:
        employees = Employee.nodes.filter(
            first_name__istartswith=first_name, last_name__istartswith=last_name
        ).order_by(orderBy)

        relationships = [
            employee.works_in.relationship(employee.works_in.get())
            for employee in employees
        ]
        filtered_relationships = [
            rel
            for rel in relationships
            if rel.position.lower().startswith(position.lower())
        ]
        filtered_employees_by_position = [
            rel.start_node() for rel in filtered_relationships
        ]

        data = [employee.get_json() for employee in filtered_employees_by_position]

        return jsonify(data)
    except Exception as e:
        return jsonify({"error_type": type(e).__name__, "message": str(e)}), 400


async def create_employee():
    data = request.get_json()

    try:
        required_fields = [
            "first_name",
            "last_name",
            "age",
            "department_name",
            "position",
            "salary",
        ]
        properties = {}

        for field in required_fields:
            property = data.get(field)
            if not property:
                raise ValueError(f"property {field} is required")
            properties[field] = property

        with db.transaction:
            department = Department.nodes.get(name=properties["department_name"])
            newEmployee = Employee.create(
                {
                    "first_name": properties["first_name"],
                    "last_name": properties["last_name"],
                    "age": properties["age"],
                }
            )[0]
            newEmployee.works_in.connect(  # type: ignore
                department,
                {"position": properties["position"], "salary": properties["salary"]},
            )

        return jsonify(newEmployee.get_json())

    except Exception as e:
        return jsonify({"error_type": type(e).__name__, "message": str(e)}), 400
