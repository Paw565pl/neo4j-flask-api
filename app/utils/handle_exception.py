from functools import wraps

from flask import jsonify


def handle_exception(func):
    @wraps(func)
    async def wrapper(*args, **kwargs):
        try:
            return await func(*args, **kwargs)
        except Exception as e:
            return jsonify({"error_type": type(e).__name__, "message": str(e)}), 400

    return wrapper
