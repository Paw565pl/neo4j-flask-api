// Tworzymy węzły Employee
CREATE (e1:Employee { first_name: 'Jan', last_name: 'Kowalski', age: 35 })
CREATE (e2:Employee { first_name: 'Anna', last_name: 'Nowak', age: 28 })
CREATE (e3:Employee { first_name: 'Piotr', last_name: 'Zieliński', age: 32 })
CREATE (e4:Employee { first_name: 'Maria', last_name: 'Wójcik', age: 30 })

// Tworzymy węzły Department
CREATE (d1:Department { name: 'IT' })
CREATE (d2:Department { name: 'HR' })
CREATE (d3:Department { name: 'Marketing' })

// Tworzymy relacje WORKS_IN
CREATE (e1)-[:WORKS_IN { position: 'Manager', salary: 10000 }]->(d1)
CREATE (e2)-[:WORKS_IN { position: 'Analyst', salary: 5000 }]->(d1)
CREATE (e3)-[:WORKS_IN { position: 'Specialist', salary: 4000 }]->(d2)
CREATE (e4)-[:WORKS_IN { position: 'Coordinator', salary: 4500 }]->(d3)

// Tworzymy relacje MANAGES
CREATE (e1)-[:MANAGES]->(e2)
CREATE (e1)-[:MANAGES]->(e3)
