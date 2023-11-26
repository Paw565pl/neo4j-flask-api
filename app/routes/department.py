from flask import jsonify, request
from models import Department


async def get_departments():
    name = request.args.get("name", "")
    order_by = request.args.get("order_by", None)

    try:
        departments = Department.nodes.filter(name__istartswith=name).order_by(order_by)
        data = [department.get_json() for department in departments]

        return jsonify(data)

    except Exception as e:
        return jsonify({"error_type": type(e).__name__, "message": str(e)}), 400
