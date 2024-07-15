# Flask REST API with Neo4j

This is a simple restful api providing CRUD operations for managing Employees and Departments.

### How to run it locally?

It is fairly simple thanks to docker. Simply run this command after **cloning the repository**.

```sh
docker compose up --build
```

If you want to seed the database with sample data you can also run this command.

```sh
docker compose exec flask flask --app app.app seed_db
```

That's all! Now simply hit [http://localhost:5000](http://localhost:5000) and enjoy using the app.

### List of endpoints

- GET (params: first_name, last_name, position, order_by), POST /employees
- GET, PUT, DELETE /employees/:uuid
- GET /employees/:uuid/subordinates
- GET (params: name, order_by), POST /departments
- GET /departments/:uuid
- GET /departments/:uuid/employees
