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


class Department(StructuredNode):
    name = StringProperty(required=True, unique_index=True)

    works_in = RelationshipFrom("Employee", "WORKS_IN", model=WorksIn, cardinality=One)  # type: ignore
