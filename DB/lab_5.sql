-- 1
drop database if exists lab5;
create database lab5;

drop table if exists customers cascade ;
create table customers
(
    customer_id serial primary key,
    cust_name   varchar(50),
    city        varchar(50),
    grade       int,
    salesman_id int
);

drop table if exists salesman cascade ;
create table salesman
(
    salesman_id serial primary key,
    name        varchar(50),
    city        varchar(50),
    commission  decimal(3, 2)
);

drop table if exists orders cascade ;
create table orders
(
    ord_no      serial primary key,
    purch_amt   decimal(10, 2),
    ord_date    date,
    customer_id int,
    salesman_id int,
    foreign key (customer_id) references customers (customer_id),
    foreign key (salesman_id) references salesman (salesman_id)
);

insert into customers (customer_id, cust_name, city, grade, salesman_id)
values (3002, 'Nick Rimando', 'New York', 100, 5001),
       (3005, 'Graham Zusi', 'California', 200, 5002),
       (3001, 'Brad Guzan', 'London', 100, 5005),
       (3004, 'Fabian Johns', 'Paris', 300, 5006),
       (3007, 'Brad Davis', 'New York', 200, 5001),
       (3009, 'Geoff Camero', 'Berlin', 100, 5003),
       (3008, 'Julian Green', 'London', 300, 5002);

insert into salesman (salesman_id, name, city, commission)
values (5001, 'James Hoog', 'New York', 0.15),
       (5002, 'Nail Knite', 'Paris', 0.13),
       (5005, 'Pit Alex', 'London', 0.11),
       (5006, 'Mc Lyon', 'Paris', 0.14),
       (5003, 'Lauson Hen', 'Berlin', 0.12),
       (5007, 'Paul Adam', 'Rome', 0.13);

insert into orders (ord_no, purch_amt, ord_date, customer_id, salesman_id)
values (70001, 150.50, '2012-10-05', 3005, 5002),
       (70009, 270.65, '2012-09-10', 3001, 5005),
       (70002, 65.26, '2012-10-05', 3002, 5001),
       (70004, 110.50, '2012-08-17', 3009, 5003),
       (70007, 948.50, '2012-09-10', 3005, 5002),
       (70005, 2400.60, '2012-07-27', 3007, 5001),
       (70008, 5760.00, '2012-09-10', 3002, 5001);

--3 Select the total purchase amount of all orders.
select sum(purch_amt) as total_purchases_amount
from orders;

--4  Select the average purchase amount of all orders.
select sum(purch_amt) / count(*) from orders;

--5 Select how many customer have listed their names.
select count(cust_name)
from customers
where cust_name is not null;

-- 6 Select the minimum purchase amount of all the orders.
select min(purch_amt)
from orders;

-- 7 Select customer with all information whose name ends with the letter 'b'.
select *
from customers
where cust_name like '%b%a%';

-- 8 Select orders which made by customers from ‘New York’.
select *
from orders
where customer_id in (select customer_id
                      from customers
                      where city = 'New York');
-- 8 Select orders which made by customers from ‘New York’.
select o.*
from orders o--2
         left join customers c--3
              on o.customer_id = c.customer_id;

-- 9 Select customers with all information who has order with purchase amount more than 10.
select *
from customers
where customer_id in (select customer_id
                      from orders
                      where purch_amt > 10);

-- 10 Select total grade of all customers.
select sum(grade) as total_grade
from customers;

-- 11 Select all customers who have listed their names.
select * from customers where cust_name is not null;

-- 12  Select the maximum grade of all the customers.
select max(grade) max_grade from customers;
