import click
from neomodel import clear_neo4j_database, db


@click.command(name="seed_db", help="Seed database with example data.")
def seed_db():
    print("seeding database...")
    with open("./app/data/sample_data.cypher", "r") as f:
        clear_neo4j_database(db)

        query = f.read()
        db.cypher_query(query)
    print("done!")
