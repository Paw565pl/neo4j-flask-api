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

    works_in = RelationshipTo("Department", "WORKS_IN", model=WorksIn, cardinality=One)
    manages = RelationshipTo("Employee", "MANAGES", model=Manages)

    def get_json(self):
        department = self.works_in.get()  # type: ignore
        works_in = self.works_in.relationship(department).__properties__  # type: ignore

        works_in["department_name"] = department.name
        works_in.pop("element_id_property")

        json = {
            "uuid": self.uuid,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "age": self.age,
            "works_in": works_in,
        }
        return json


class Department(StructuredNode):
    uuid = UniqueIdProperty()
    name = StringProperty(required=True, unique_index=True)

    works_in = RelationshipFrom("Employee", "WORKS_IN", model=WorksIn)

    def get_json(self):
        json = {"uuid": self.uuid, "name": self.name}
        return json
