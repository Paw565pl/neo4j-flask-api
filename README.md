# Live demo

[Hosted on render.com](https://neo4j-flask-api-5isw.onrender.com/employees)

### How to run it locally?

1. Create .env file looking something like that

```
NEO4J_BOLT_URL=bolt://neo4j:neo4j@localhost:7687
```

2. Install dependencies in your python virtualenv

```
pip install -r requirements.txt
```

3. Run the server

```
flask --app app.app run --debug
```

4. Optionally seed the database

```
flask --app app.app seed_db
```

5. You are good to go!

### List of endpoints

- GET (params: first_name, last_name, position, order_by), POST /employees
- GET, PUT, DELETE /employees/:uuid
- GET /employees/:uuid/subordinates
- GET (params: name, order_by) /departments
- GET /departments/:uuid
- GET /departments/:uuid/employees
