-- **********************
-- create customer table
-- **********************

-- create table customer(
-- customer_id serial primary key,
-- first_name varchar(50) NOT NULL,
-- last_name varchar(100) NOT NULL
-- )

-- Insert into customer(first_name, last_name)
-- values
-- 	('John', 'Doe'),
-- 	('Jerome', 'Lalu'),
-- 	('Lea', 'Rive')


-- select *
-- from customer


-- *******************************
-- create customer_profile table
-- *******************************

-- create table customer_profile(
-- profile_id serial primary key,
-- isLoggedIn boolean DEFAULT false,
-- customer_id int unique references customer(customer_id)
-- )

-- Insert into customer_profile(isLoggedIn, customer_id)
-- values
-- 	('True', (select customer_id from customer where first_name = 'John')),
-- 	('False', (select customer_id from customer where first_name = 'Jerome'))


-- select *
-- from customer_profile


-- *******************************************
-- Use the relevant types of Joins to display
-- *******************************************

-- The first_name of the LoggedIn customers

-- select c.first_name
-- from customer as c
-- left join customer_profile as cp
-- on cp.customer_id = c.customer_id
-- where isloggedin = 'true'


-- All the customers first_name and isLoggedIn columns - even the customers those who don’t have a profile.

-- select c.first_name, cp.isLoggedIn
-- from customer as c
-- left join customer_profile as cp
-- on cp.customer_id = c.customer_id


-- The number of customers that are not LoggedIn

select count(*)
from customer as c
left join customer_profile as cp
on cp.customer_id = c.customer_id
where isLoggedIn = 'false' or isLoggedIn is null