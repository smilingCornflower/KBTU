drop database if exists lab3;
create database lab3;


select lastname
from employees;

select distinct lastname
from employees;

select *
from employees
where lastname = 'Smith';

select *
from employees
where lastname in ('Smith', 'Doe');

select *
from employees
where department = 14;

select *
from employees
where department IN (37, 77);

select sum(budget) as total_budget
from departments;

select department, count(*) as employees_number
from employees
group by department;

select department, count(*) as employees_number
from employees
group by department
having count(*) > 2;

select name
from departments
order by budget desc
offset 1 limit 1;

select name, lastname
from employees
where department = (select code
                    from departments
                    order by budget
                    limit 1);


select name, 'employees' as type
from employees
where city = 'Almaty'
union
select name, 'customers' as type
from customers
where city = 'Almaty';

select *
from departments
where budget > 60000
order by budget, code desc;

update departments
set budget = budget * 0.9
where code = (select code
              from departments
              order by budget
              limit 1);

update employees
set department = (select code
                  from departments
                  where name = 'IT')
where department = (select code
                    from departments
                    where name = 'Research');

delete
from employees
where department = (select code
                    from departments
                    where name = 'IT');


-- noinspection SqlWithoutWhere
delete from employees;