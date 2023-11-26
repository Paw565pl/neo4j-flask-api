from flask import jsonify, request
from models import Department, Employee
from neomodel import db


async def get_employees():
    first_name = request.args.get("first_name", "")
    last_name = request.args.get("last_name", "")
    position = request.args.get("position", "")
    order_by = request.args.get("order_by", None)

    try:
        employees = Employee.nodes.filter(
            first_name__istartswith=first_name, last_name__istartswith=last_name
        ).order_by(order_by)

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
    body = request.get_json()

    try:
        properties = await _validate_request_body(body)

        with db.transaction:
            new_employee = Employee()
            new_employee.first_name = properties["first_name"]
            new_employee.last_name = properties["last_name"]
            new_employee.age = properties["age"]
            new_employee.save()

            department = Department.nodes.get(name=properties["department_name"])

            new_employee.works_in.connect(
                department,
                {"position": properties["position"], "salary": properties["salary"]},
            )

        return jsonify(new_employee.get_json()), 201

    except Exception as e:
        return jsonify({"error_type": type(e).__name__, "message": str(e)}), 400


async def update_employee(uuid):
    body = request.get_json()

    try:
        properties = await _validate_request_body(body)

        with db.transaction:
            employee = Employee.nodes.get(uuid=uuid)
            employee.first_name = properties["first_name"]
            employee.last_name = properties["last_name"]
            employee.age = properties["age"]
            employee.save()

            old_department = employee.works_in.get()
            rel = employee.works_in.relationship(old_department)

            rel.position = properties["position"]
            rel.salary = properties["salary"]
            rel.save()

            new_department = Department.nodes.get(name=properties["department_name"])
            employee.works_in.reconnect(old_department, new_department)

        return jsonify(employee.get_json())

    except Exception as e:
        return jsonify({"error_type": type(e).__name__, "message": str(e)}), 400


async def delete_employee(uuid):
    try:
        employee = Employee.nodes.get(uuid=uuid)

        if len(employee.manages) != 0:
            return (
                jsonify(
                    {
                        "message": "this employee can not be deleted, because he is associated with one or more subordinates"
                    }
                ),
                405,
            )

        employee.delete()
        return jsonify({"message": "employee removed successfully"})

    except Exception as e:
        return jsonify({"error_type": type(e).__name__, "message": str(e)}), 400


async def get_employee_subordinates(uuid):
    try:
        results, _ = db.cypher_query(
            "MATCH (n:Employee {uuid: $uuid})-[:MANAGES]->(m:Employee) RETURN m",
            params={"uuid": uuid},
            resolve_objects=True,
        )

        response = [employee[0].get_json() for employee in results]
        return jsonify(response)

    except Exception as e:
        return jsonify({"error_type": type(e).__name__, "message": str(e)}), 400


async def _validate_request_body(body):
    required_fields = [
        "first_name",
        "last_name",
        "age",
        "department_name",
        "position",
        "salary",
    ]
    data = {}

    for field in required_fields:
        param = body.get(field)
        if not param:
            raise ValueError(f"property {field} is required")
        data[field] = param

    return data
