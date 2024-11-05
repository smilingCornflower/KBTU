DROP DATABASE IF EXISTS lab6;
CREATE DATABASE lab6;

DROP TABLE IF EXISTS locations CASCADE;
CREATE TABLE locations
(
    location_id    SERIAL PRIMARY KEY,
    street_address VARCHAR(25),
    postal_code    VARCHAR(12),
    city           VARCHAR(30),
    state_province VARCHAR(12)
);

DROP TABLE IF EXISTS departments CASCADE;
CREATE TABLE departments
(
    department_id   SERIAL PRIMARY KEY,
    department_name VARCHAR(50) UNIQUE,
    budget          INTEGER,
    location_id     INTEGER REFERENCES locations
);

DROP TABLE IF EXISTS employees CASCADE;
CREATE TABLE employees
(
    employee_id   SERIAL PRIMARY KEY,
    first_name    VARCHAR(50),
    last_name     VARCHAR(50),
    email         VARCHAR(50),
    phone_number  VARCHAR(20),
    salary        INTEGER,
    department_id INTEGER REFERENCES departments
);

INSERT INTO locations (street_address, postal_code, city, state_province)
VALUES ('123 Main St', '12345', 'New York', 'NY'),
       ('456 Elm St', '54321', 'Los Angeles', 'CA'),
       ('789 Oak St', '67890', 'Chicago', 'IL'),
       ('101 Pine St', '11223', 'Houston', 'TX'),
       ('202 Cedar St', '33445', 'Phoenix', 'AZ'),
       ('303 Maple St', '55667', 'Philadelphia', 'PA'),
       ('404 Birch St', '77889', 'San Antonio', 'TX');

INSERT INTO departments (department_name, budget, location_id)
VALUES ('Engineering', 500000, 1),
       ('Marketing', 200000, 2),
       ('Sales', 300000, 3),
       ('HR', 150000, 1),
       ('Finance', 400000, 4),
       ('IT', 350000, 5),
       ('Customer Service', 250000, 6),
       ('Research', 450000, 7);

INSERT INTO employees (first_name, last_name, email, phone_number, salary, department_id)
VALUES ('John', 'Doe', 'john.doe@example.com', '555-1234', 70000, 1),
       ('Jane', 'Smith', 'jane.smith@example.com', '555-5678', 80000, 2),
       ('Michael', 'Johnson', 'michael.j@example.com', '555-8765', 75000, 3),
       ('Emily', 'Davis', 'emily.d@example.com', '555-4321', 60000, 4),
       ('Robert', 'Brown', 'robert.b@example.com', '555-1111', 95000, 5),
       ('Jessica', 'Taylor', 'jessica.t@example.com', '555-2222', 67000, 6),
       ('William', 'Anderson', 'william.a@example.com', '555-3333', 88000, 7),
       ('Linda', 'Thomas', 'linda.t@example.com', '555-4444', 91000, 1),
       ('Barbara', 'Harris', 'barbara.h@example.com', '555-5555', 72000, 2),
       ('Richard', 'Clark', 'richard.c@example.com', '555-6666', 83000, 3),
       ('Susan', 'Lewis', 'susan.l@example.com', '555-7777', 79000, 4),
       ('Joseph', 'Walker', 'joseph.w@example.com', '555-8888', 56000, 5),
       ('Karen', 'Hall', 'karen.h@example.com', '555-9999', 64000, 6),
       ('James', 'Allen', 'james.a@example.com', '555-0000', 92000, 7),
       ('Patricia', 'Young', 'patricia.y@example.com', '555-1010', 86000, 1);


-- 3. Select the first name, last name, department id, and department name for each employee.
SELECT e.first_name, e.last_name, e.department_id, d.department_name
FROM employees e
         JOIN departments d
              ON e.department_id = d.department_id;


-- 4. Select the first name, last name, department id and department name,
-- for all employees for departments 80 or 40.
SELECT e.first_name, e.last_name, e.department_id, d.department_name
FROM employees e
         JOIN departments d
              ON e.department_id = d.department_id
WHERE d.department_id IN (40, 80);

-- 5. Select the first and last name, department, city, and state province for each employee.
SELECT e.first_name, e.last_name, d.department_name, l.city, l.state_province
FROM employees e
         JOIN departments d
              ON e.department_id = d.department_id
         JOIN locations l ON d.location_id = l.location_id;

-- 6. Select all departments including those where does not have any employee.
SELECT d.*
FROM departments d
         LEFT JOIN employees e on d.department_id = e.department_id;


-- 7. Select the first name, last name, department id and name,
-- for all employees who have or have not any department.
SELECT e.* FROM employees e
LEFT JOIN departments d
ON e.department_id = d.department_id;
