from flask import jsonify, request
from neomodel import clear_neo4j_database, db


def seed_db():
    data = request.get_json()
    seedAgree = data.get("seed")

    if not seedAgree and seedAgree != "yes":
        return jsonify({}), 400

    with open("./app/data/seed_data.cypher", "r") as queryFile:
        clear_neo4j_database(db)

        queryFileString = queryFile.read()
        db.cypher_query(queryFileString)

        return jsonify({"message": "database seeded successfully"}), 201
