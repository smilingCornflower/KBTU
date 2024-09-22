-- 1
DROP DATABASE IF EXISTS lab_2;
CREATE DATABASE lab_2;

-- 2
DROP TABLE IF EXISTS countries CASCADE;
CREATE TABLE countries (
    country_id SERIAL PRIMARY KEY,
    country_name  VARCHAR(100),
    region_id INTEGER,
    population INTEGER
);

-- 3
INSERT INTO countries (country_name, region_id, population)
VALUES ('France', 1, 67000000);

-- 4
INSERT INTO countries (country_id, country_name)
VALUES (DEFAULT, 'Germany');

-- 5
INSERT INTO countries (country_name, region_id, population)
VALUES ('Spain', NULL, 47000000);

-- 6
INSERT INTO countries (country_name, region_id, population)
VALUES
('USA', 2, 331000000),
('Italy', 3, 60000000),
('Japan', 4, 126000000);

-- 7
ALTER TABLE countries
ALTER COLUMN country_name SET DEFAULT 'Kazakhstan';

-- 8
INSERT INTO countries (country_name, region_id, population)
VALUES (DEFAULT, 5, 19000000);

-- 9
INSERT INTO countries (country_name, region_id, population)
VALUES (DEFAULT, DEFAULT, DEFAULT);

-- 10
DROP TABLE IF EXISTS countries_new CASCADE;
CREATE TABLE countries_new (LIKE countries INCLUDING ALL);

-- 11
INSERT INTO countries_new SELECT * FROM countries;

-- 12
UPDATE countries
SET region_id = 1
WHERE region_id is NULL;

-- 13
UPDATE countries
SET population = population * 1.1
WHERE country_id >= 0
RETURNING country_name, population AS "New Population";

-- 14
DELETE FROM countries
WHERE population < 100000;

-- 15
DELETE FROM countries_new
USING countries
WHERE countries_new.country_id = countries.country_id
RETURNING countries_new.*;

-- 16
DELETE FROM countries
WHERE country_id > -1
RETURNING *;