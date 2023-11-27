import aiofiles
from flask import jsonify, request, Blueprint
from neomodel import clear_neo4j_database, db
from utils.handle_exception import handle_exception

seed_blueprint = Blueprint("seed", __name__)


@seed_blueprint.post("/")
@handle_exception
async def seed_db():
    data = request.get_json()
    seed_agree = data.get("seed")

    if not seed_agree and seed_agree != "yes":
        return jsonify({}), 400

    async with aiofiles.open("./app/data/seed_data.cypher", "r") as queryFile:
        clear_neo4j_database(db)

        query_file_string = await queryFile.read()
        db.cypher_query(query_file_string)

        return jsonify({"message": "database seeded successfully"}), 201
