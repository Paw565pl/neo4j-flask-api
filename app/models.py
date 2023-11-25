from neomodel import (
    FloatProperty,
    IntegerProperty,
    RelationshipFrom,
    RelationshipTo,
    StringProperty,
    StructuredNode,
    StructuredRel,
)
from neomodel.cardinality import One


class Manages(StructuredRel):
    pass


class WorksIn(StructuredRel):
    position = StringProperty(required=True)
    salary = FloatProperty(required=True)


class Employee(StructuredNode):
    first_name = StringProperty(required=True, unique_index=True)
    last_name = StringProperty(required=True, unique_index=True)
    age = IntegerProperty(required=True)

    works_in = RelationshipTo("Department", "WORKS_IN", model=WorksIn, cardinality=One)  # type: ignore
    manages = RelationshipTo("Employee", "MANAGES", model=Manages)

    def get_json(self):
        department_name = self.works_in.get().__properties__["name"]  # type: ignore
        works_in = self.works_in.relationship(self.works_in.get()).__properties__  # type: ignore

        works_in["department_name"] = department_name
        works_in.pop("element_id_property")

        json = {
            "id": self.element_id,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "age": self.age,
            "works_in": works_in,
        }
        return json


class Department(StructuredNode):
    name = StringProperty(required=True, unique_index=True)

    works_in = RelationshipFrom("Employee", "WORKS_IN", model=WorksIn, cardinality=One)  # type: ignore
