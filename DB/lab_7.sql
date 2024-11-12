drop table if exists departments cascade;
create table departments
(
    department_id serial primary key,
    name          varchar(50)    not null,
    budget        numeric(12, 2) not null
);

drop table if exists countries cascade;
create table countries
(
    id   serial primary key,
    name varchar(100) not null
);

insert into countries (name)
values ('Kazakhstan'),
       ('Russia'),
       ('United States'),
       ('Canada'),
       ('China'),
       ('India'),
       ('Brazil'),
       ('United Kingdom'),
       ('Australia'),
       ('Germany');

drop table if exists employees cascade;

create table employees
(
    id            serial primary key,
    name          varchar(50) not null,
    surname       varchar(50) not null,
    salary        numeric(12, 2),
    department_id integer
);

insert into employees (name, surname, salary, department_id)
values ('John', 'Doe', 55000.00, 1),
       ('Jane', 'Smith', 62000.00, 2),
       ('Michael', 'Johnson', 72000.00, 1),
       ('Emily', 'Davis', 50000.00, 3),
       ('David', 'Wilson', 61000.00, 2),
       ('Sarah', 'Brown', 53000.00, 1),
       ('Chris', 'Miller', 67000.00, 2),
       ('Jessica', 'Taylor', 75000.00, 3),
       ('Daniel', 'Anderson', 59000.00, 1),
       ('Laura', 'Thomas', 68000.00, 2);



-- 1.   Create index for queries like below:
--      SELECT * FROM countries WHERE name = ‘string’;
create index c_name_index on countries (name);


-- 2.   Create index for queries like below:
--      SELECT * FROM employees WHERE name = ‘string’ AND surname = ‘string’;
create index e_fullname_index on employees (name, surname);

-- 3.   Create unique index for queries like below:
--      SELECT * FROM employees WHERE salary < value1 AND salary > value2;
create unique index e_salary_uindex on employees (salary);

-- 4.   Create index for queries like below:
--      SELECT * FROM employees WHERE substring(name from 1 for 4) = ‘abcd’;
create index e_subname_index on employees (substring(name from 1 for 4));

-- 5.   Create index for queries like below:
--      SELECT * FROM employees e JOIN departments d
--          ON d.department_id = e.department_id
--          WHERE d.budget > value2 AND e.salary < value2;
create index d_id_index on departments (department_id);
create index d_budget_index on departments (budget);

create index e_id_index on employees (department_id);
create index e_salary_index on employees (salary);

