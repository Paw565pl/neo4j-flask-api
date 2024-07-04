from flask import jsonify
from neomodel import DoesNotExist, RequiredProperty


def exception_handler(e: Exception):
    if isinstance(e, DoesNotExist):
        return jsonify({"message": "not found"}), 404
    elif isinstance(e, ValueError):
        return jsonify({"message": str(e)}), 400
    elif isinstance(e, RequiredProperty):
        return jsonify({"message": f"{e.property_name} is required"}), 400
    else:
        return jsonify({"error_type": type(e).__name__, "message": str(e)}), 500
