// Tworzymy węzły Employee
CREATE (e1:Employee { first_name: 'Jan', last_name: 'Kowalski', age: 35 })
CREATE (e2:Employee { first_name: 'Anna', last_name: 'Nowak', age: 28 })
CREATE (e3:Employee { first_name: 'Piotr', last_name: 'Zieliński', age: 32 })
CREATE (e4:Employee { first_name: 'Maria', last_name: 'Wójcik', age: 30 })
CREATE (e5:Employee { first_name: 'Robert', last_name: 'Lewandowski', age: 37 })
CREATE (e6:Employee { first_name: 'Jac', last_name: 'Muchowski', age: 52 })
CREATE (e7:Employee { first_name: 'Aleksandra', last_name: 'Kowalska', age: 22 })
CREATE (e8:Employee { first_name: 'Tomasz', last_name: 'Smok', age: 29 })
CREATE (e9:Employee { first_name: 'Sławomir', last_name: 'Piątek', age: 33 })
CREATE (e10:Employee { first_name: 'Jacek', last_name: 'Soplica', age: 41 })

// Tworzymy węzły Department
CREATE (d1:Department { name: 'IT' })
CREATE (d2:Department { name: 'HR' })
CREATE (d3:Department { name: 'Marketing' })

// Tworzymy relacje WORKS_IN
CREATE (e1)-[:WORKS_IN { position: 'Manager', salary: 10000 }]->(d1)
CREATE (e2)-[:WORKS_IN { position: 'Analyst', salary: 5000 }]->(d1)
CREATE (e3)-[:WORKS_IN { position: 'Specialist', salary: 4000 }]->(d2)
CREATE (e4)-[:WORKS_IN { position: 'Coordinator', salary: 4500 }]->(d3)
CREATE (e5)-[:WORKS_IN { position: 'Coordinator', salary: 4500 }]->(d3)
CREATE (e6)-[:WORKS_IN { position: 'Senior Developer', salary: 12500 }]->(d1)
CREATE (e7)-[:WORKS_IN { position: 'Recruiter', salary: 4600 }]->(d2)
CREATE (e8)-[:WORKS_IN { position: 'Recruiter', salary: 3800 }]->(d2)
CREATE (e9)-[:WORKS_IN { position: 'Manager', salary: 8900 }]->(d3)
CREATE (e10)-[:WORKS_IN { position: 'Secretary', salary: 4500 }]->(d3)

// Tworzymy relacje MANAGES
CREATE (e1)-[:MANAGES]->(e2)
CREATE (e1)-[:MANAGES]->(e6)
CREATE (e9)-[:MANAGES]->(e10)
