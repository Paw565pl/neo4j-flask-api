from flask import jsonify, request
from models import Employee


async def employees():
    first_name = request.args.get("first_name", "")
    last_name = request.args.get("last_name", "")
    position = request.args.get("position", "")
    orderBy = request.args.get("order_by", None)

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
