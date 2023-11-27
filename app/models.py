from neomodel import (
    FloatProperty,
    IntegerProperty,
    RelationshipFrom,
    RelationshipTo,
    StringProperty,
    StructuredNode,
    StructuredRel,
    UniqueIdProperty,
)
from neomodel.cardinality import One


class Manages(StructuredRel):
    pass


class WorksIn(StructuredRel):
    position = StringProperty(required=True)
    salary = FloatProperty(required=True)


class Employee(StructuredNode):
    uuid = UniqueIdProperty()
    first_name = StringProperty(required=True, unique_index=True)
    last_name = StringProperty(required=True, unique_index=True)
    age = IntegerProperty(required=True)

    works_in = RelationshipTo("Department", "WORKS_IN", model=WorksIn, cardinality=One)  # type: ignore
    manages = RelationshipTo("Employee", "MANAGES", model=Manages)

    def get_json(self):
        department = self.works_in.get()  # type: ignore
        works_in = self.works_in.relationship(department)  # type: ignore

        json = {
            "uuid": self.uuid,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "age": self.age,
            "works_in": {
                "department_name": department.name,
                "position": works_in.position,
                "salary": works_in.salary,
            },
        }
        return json


class Department(StructuredNode):
    uuid = UniqueIdProperty()
    name = StringProperty(required=True, unique_index=True)

    works_in = RelationshipFrom("Employee", "WORKS_IN", model=WorksIn)

    def get_json(self):
        employees = self.works_in.all()  # type: ignore
        managers = [
            {k: v for k, v in employee.get_json().items() if k != "works_in"}
            for employee in employees
            if employee.manages
        ]

        json = {
            "uuid": self.uuid,
            "name": self.name,
            "employees_count": len(employees),
            "managers": managers,
        }
        return json
