<<<<<<< HEAD
--Test

--HOW TO CREATE A TABLE

-- CREATE TABLE actors(
-- actors_id SERIAL PRIMARY KEY,
-- first_name VARCHAR(50) NOT NULL,
-- last_name VARCHAR(100) NOT NULL,
-- birth_day DATE NOT NULL,
-- number_oscars SMALLINT
-- )


--HOW TO INSERT DATA

-- INSERT INTO actors(first_name, last_name, birth_day, number_oscars)
-- VALUES ('Matt', 'Damon', '08/10/1970', 5) 

-- INSERT INTO actors(first_name, last_name, birth_day, number_oscars)
-- VALUES ('Julianne', 'Moore', '03/12/1960', 1) 

-- INSERT INTO actors(first_name, last_name, birth_day, number_oscars)
-- VALUES ('Helen', 'Mirren', '26/07/1945', 1) 

-- INSERT INTO actors (first_name, last_name, birth_day, number_oscars)
-- VALUES
-- 	('Colin', 'Firth', '10/09/1960', 1),
-- 	('Nicolas', 'Cage', '07/01/1964', 1),
-- 	('Meryl', 'Streep', '22/07/1949', 3),
-- 	('Jodie', 'Foster', '19/11/1962', 2),
-- 	('Emma', 'Stone', '06/11/1988', 2)

-- DELETE FROM actors
-- WHERE first_name = 'Matt' AND last_name = 'Mirren'

-- INSERT INTO actors(first_name, last_name, birth_day, number_oscars)
-- VALUES ('Natalie', 'Portman', '09/06/1981', NULL) 


--DIFFERENT WAYS OF RETRRIEVING THE DATA
-- SELECT first_name, number_oscars
-- FROM actors

-- SELECT *
-- FROM actors
-- WHERE number_oscars > 2

-- SELECT *
-- FROM actors
-- WHERE number_oscars = 2 AND first_name = 'Jodie'

-- SELECT *
-- FROM actors
-- WHERE (number_oscars = 2 AND first_name = 'Jodie') AND last_name = 'Foster'

-- SELECT *
-- FROM actors
-- WHERE number_oscars IS NULL

-- SELECT first_name
-- FROM actors
-- WHERE last_name LIKE '%p' --ends

-- SELECT first_name
-- FROM actors
-- WHERE last_name ILIKE 's%' --starts

-- SELECT *
-- FROM actors
-- WHERE number_oscars > 2 
-- LIMIT 1

-- SELECT first_name
-- FROM actors
-- ORDER BY first_name DESC -- DESC - from high to low

-- DELERE A RECORD

--DELETE FROM actors
--WHERE actor_id = 6

--ALTER A TABLE (CHANGE)
-- ALTER TABLE actors
-- RENAME COLUMN number_oscars TO oscars

=======
--Test

--HOW TO CREATE A TABLE

-- CREATE TABLE actors(
-- actors_id SERIAL PRIMARY KEY,
-- first_name VARCHAR(50) NOT NULL,
-- last_name VARCHAR(100) NOT NULL,
-- birth_day DATE NOT NULL,
-- number_oscars SMALLINT
-- )


--HOW TO INSERT DATA

-- INSERT INTO actors(first_name, last_name, birth_day, number_oscars)
-- VALUES ('Matt', 'Damon', '08/10/1970', 5) 

-- INSERT INTO actors(first_name, last_name, birth_day, number_oscars)
-- VALUES ('Julianne', 'Moore', '03/12/1960', 1) 

-- INSERT INTO actors(first_name, last_name, birth_day, number_oscars)
-- VALUES ('Helen', 'Mirren', '26/07/1945', 1) 

-- INSERT INTO actors (first_name, last_name, birth_day, number_oscars)
-- VALUES
-- 	('Colin', 'Firth', '10/09/1960', 1),
-- 	('Nicolas', 'Cage', '07/01/1964', 1),
-- 	('Meryl', 'Streep', '22/07/1949', 3),
-- 	('Jodie', 'Foster', '19/11/1962', 2),
-- 	('Emma', 'Stone', '06/11/1988', 2)

-- DELETE FROM actors
-- WHERE first_name = 'Matt' AND last_name = 'Mirren'

-- INSERT INTO actors(first_name, last_name, birth_day, number_oscars)
-- VALUES ('Natalie', 'Portman', '09/06/1981', NULL) 


--DIFFERENT WAYS OF RETRRIEVING THE DATA
-- SELECT first_name, number_oscars
-- FROM actors

-- SELECT *
-- FROM actors
-- WHERE number_oscars > 2

-- SELECT *
-- FROM actors
-- WHERE number_oscars = 2 AND first_name = 'Jodie'

-- SELECT *
-- FROM actors
-- WHERE (number_oscars = 2 AND first_name = 'Jodie') AND last_name = 'Foster'

-- SELECT *
-- FROM actors
-- WHERE number_oscars IS NULL

-- SELECT first_name
-- FROM actors
-- WHERE last_name LIKE '%p' --ends

-- SELECT first_name
-- FROM actors
-- WHERE last_name ILIKE 's%' --starts

-- SELECT *
-- FROM actors
-- WHERE number_oscars > 2 
-- LIMIT 1

-- SELECT first_name
-- FROM actors
-- ORDER BY first_name DESC -- DESC - from high to low

-- DELERE A RECORD

--DELETE FROM actors
--WHERE actor_id = 6

--ALTER A TABLE (CHANGE)
-- ALTER TABLE actors
-- RENAME COLUMN number_oscars TO oscars

>>>>>>> 2776dc4e113263810fb20e4c4a72163f75a3b899
-- DROP TABLE IF EXISTS actors