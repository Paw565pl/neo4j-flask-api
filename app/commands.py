import click
from neomodel import clear_neo4j_database, db


@click.command(name="seed_db", help="Seed database with example data.")
def seed_db():
    print("seeding database...")
    with open("./app/data/seed_data.cypher", "r") as queryFile:
        clear_neo4j_database(db)

        query_file_string = queryFile.read()
        db.cypher_query(query_file_string)
    print("done!")
