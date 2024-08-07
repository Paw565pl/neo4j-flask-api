CREATE (e1:Employee { first_name: 'John', last_name: 'Smith', age: 35, uuid: randomUUID() })
CREATE (e2:Employee { first_name: 'Anna', last_name: 'West', age: 28, uuid: randomUUID() })
CREATE (e3:Employee { first_name: 'Kanye', last_name: 'East', age: 32, uuid: randomUUID() })
CREATE (e4:Employee { first_name: 'Mary', last_name: 'Jane', age: 30, uuid: randomUUID() })
CREATE (e5:Employee { first_name: 'Robert', last_name: 'Lewandowski', age: 37, uuid: randomUUID() })
CREATE (e6:Employee { first_name: 'Jack', last_name: 'Fly', age: 52, uuid: randomUUID() })
CREATE (e7:Employee { first_name: 'Alexandra', last_name: 'Monday', age: 22, uuid: randomUUID() })
CREATE (e8:Employee { first_name: 'Thomas', last_name: 'Dragon', age: 29, uuid: randomUUID() })
CREATE (e9:Employee { first_name: 'John', last_name: 'Friday', age: 33, uuid: randomUUID() })
CREATE (e10:Employee { first_name: 'Jack', last_name: 'Soplica', age: 41, uuid: randomUUID() })

CREATE (d1:Department { name: 'IT', uuid: randomUUID() })
CREATE (d2:Department { name: 'HR', uuid: randomUUID() })
CREATE (d3:Department { name: 'Marketing', uuid: randomUUID() })

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

CREATE (e1)-[:MANAGES]->(e2)
CREATE (e1)-[:MANAGES]->(e6)
CREATE (e9)-[:MANAGES]->(e10)
