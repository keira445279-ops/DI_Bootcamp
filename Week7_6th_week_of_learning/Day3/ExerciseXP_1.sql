-- ==============================
-- Exercise 1: DVD Rental
-- ==============================


-- **********************************************************************
-- 1. Get a list of all the languages, from the language table.
-- **********************************************************************

-- select name
-- from language


-- **********************************************************************
-- 2. Get a list of all films joined with their languages – select the 
-- following details : film title, description, and language name.
-- **********************************************************************

-- select f.title, f.description, l.name
-- from film as f
-- inner join language as l
-- on l.language_id = f.language_id


-- **************************************************************************
-- 3. Get all languages, even if there are no films in those languages – 
--select the following details : film title, description, and language name.
-- **************************************************************************

-- select f.title, f.description, l.name
-- from film as f
-- right join language as l
-- on l.language_id = f.language_id


-- **************************************************************************
-- 4. Create a new table called new_film with the following columns : 
-- id, name. Add some new films to the table.
-- **************************************************************************

-- create table new_film(
-- film_id serial primary key,
-- film_name varchar(50)
-- )

-- insert into new_film (film_name)
-- values ('Casablanca'), ('Cinderella Story'), ('Wicked'), ('Avatar')

-- select *
-- from new_film


-- ******************************************************************************************************
-- 5. Create a new table called customer_review, which will contain film reviews that customers will make.
-- Think about the DELETE constraint: if a film is deleted, its review should be automatically deleted.
-- It should have the following columns:
-- 5.1. review_id – a primary key, non null, auto-increment. +
-- 5.2. film_id – references the new_film table. The film that is being reviewed. +
-- 5.3. language_id – references the language table. What language the review is in. +
-- 5.4. title – the title of the review.
-- 5.5. score – the rating of the review (1-10).
-- 5.6. review_text – the text of the review. No limit on the length.
-- 5.7. last_update – when the review was last updated.
-- ******************************************************************************************************

-- create table customer_review(
-- review_id serial not null primary key,
-- film_id int references new_film (film_id) ON DELETE CASCADE,
-- language_id int references language (language_id),
-- title varchar(100),
-- score smallint not null,
-- review_text text,
-- last_update timestamp default current_timestamp
-- )


-- ******************************************************************************************************
-- 6. Add 2 movie reviews. Make sure you link them to valid objects in the other tables.
-- ******************************************************************************************************

-- insert into customer_review (film_id, language_id, title, score, review_text)
-- values
-- 	((select film_id from new_film where film_name = 'Casablanca'),
-- 	(select language_id from language where name = 'English'),
-- 	'Casablanca review', 10, 'The film was very good and very sad.'),
-- 	((select film_id from new_film where film_name = 'Cinderella Story'),
-- 	(select language_id from language where name = 'German'),
-- 	'Our Cinderella', 7, 'You can watch this film with familt. It is good.'),
-- 	((select film_id from new_film where film_name = 'Wicked'),
-- 	(select language_id from language where name = 'English'),
-- 	'Wicked review', 8, 'The film is good, Ariana Grande is nice actress.'),
-- 	((select film_id from new_film where film_name = 'Avatar'),
-- 	(select language_id from language where name = 'French'),
-- 	'Avatar review', 9, 'Like it is our reality')

-- select *
-- from customer_review


-- *******************************************************************************************************
-- 7. Delete a film that has a review from the new_film table, what happens to the customer_review table?
-- *******************************************************************************************************

-- delete from new_film where film_name = 'Cinderella Story'

-- select *
-- from customer_review




