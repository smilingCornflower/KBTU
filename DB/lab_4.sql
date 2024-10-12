-- 1
drop database if exists lab_4;
create database lab_4;

-- 2
drop table if exists warehouses cascade;
create table warehouses
(
    code     serial p
        rimary key,
    location varchar(255),
    capacity int
);

drop table if exists boxes cascade;
create table boxes
(
    code      char(4) primary key,
    contents  varchar(255),
    value     real,
    warehouse integer references warehouses (code)
);

-- 3
insert into warehouses (location, capacity)
values ('Chicago', 3),
       ('Chicago', 4),
       ('New York', 7),
       ('Los Angeles', 2),
       ('San Francisco', 8);

insert into boxes (code, contents, value, warehouse)
values ('0MN7', 'Rocks', 180, 3),
       ('4H8P', 'Rocks', 250, 1),
       ('4RT3', 'Scissors', 190, 4),
       ('7G3H', 'Rocks', 200, 1),
       ('8JN6', 'Papers', 75, 1),
       ('8Y6U', 'Papers', 50, 3),
       ('9J6F', 'Papers', 175, 2),
       ('LL08', 'Rocks', 140, 4),
       ('P0H6', 'Scissors', 125, 1),
       ('P2T6', 'Scissors', 150, 2),
       ('TU55', 'Papers', 90, 5);

-- 4
select *
from warehouses;

-- 5
select *
from boxes
where value > 150;

-- 6
select distinct contents
from boxes;

-- 7
select warehouse, contents, count(*) as boxes_count
from boxes group by warehouse;
                  --, contents;


select warehouse, count(*) as boxes_count
from boxes
group by warehouse;

-- 8
select warehouse, count(*) as boxes_count
from boxes where value > 150
group by warehouse
having count(*) > 2;

-- 9
insert into warehouses (location, capacity)
values ('New York', 3);

-- 10
insert into boxes (code, contents, value, warehouse)
values ('H5RT', 'Papers', 200, 2);

-- 11
update boxes a
set value = value * 0.85
where code in (select b.code
              from boxes b
              where b.code = a.code              order by value desc
              offset 2 limit 1);


-- 12
delete
from boxes
where value < 150;

-- 13
delete
from boxes
where warehouse = (select code
                   from warehouses
                   where location = 'New York')
returning *;
