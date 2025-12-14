-- create table

-- CREATE TABLE actors(
-- actors_id SERIAL PRIMARY KEY,
-- first_name VARCHAR(50) NOT NULL,
-- last_name VARCHAR(100) NOT NULL,
-- birth_day DATE NOT NULL,
-- number_oscars SMALLINT
-- )

-- create values

-- INSERT INTO actors(first_name, last_name, birth_day, number_oscars)
-- VALUES 
-- 	('Matt', 'Damon', '08/10/1970', 5), 
-- 	('Julianne', 'Moore', '03/12/1960', 1),
-- 	('Helen', 'Mirren', '26/07/1945', 1),
-- 	('Colin', 'Firth', '10/09/1960', 1),
-- 	('Nicolas', 'Cage', '07/01/1964', 1),
-- 	('Meryl', 'Streep', '22/06/1949', 3),
-- 	('Jodie', 'Foster', '19/11/1962', 2),
-- 	('Emma', 'Stone', '06/11/1988', 2),
-- 	('Natalie', 'Portman', '09/06/1981', NULL) 

-- Count how many actors are in the table

-- SELECT COUNT(*)
-- FROM actors

-- Try to add a new actor with some blank fields. What do you think the outcome will be ?

-- INSERT INTO actors (first_name, last_name, birth_day, number_oscars)
-- VALUES ('Tom', '', '01/06/1996', NULL) 

-- IF VARCHAR WOULD BE EMPTY, IN THE OUTCOME THE COLUMN WIL BE EMPTY

-- INSERT INTO actors (first_name, last_name, birth_day, number_oscars)
-- VALUES ('Daniel', 'Radcliff', '23/07/1989', NULL)

-- IF THE NUMBER OF OSCARS WOULD BE EMPTY, THEN WE COULDN`T UPDATE THE TABLE AND WE NEED TO ADD NULL

-- SELECT *
-- FROM actors

 