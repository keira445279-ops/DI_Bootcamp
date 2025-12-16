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



-- ==============================
-- Exercise 2: DVD Rental
-- ==============================

-- *******************************************************************************************************
-- 1. Use UPDATE to change the language of some films. Make sure that you use valid languages.
-- *******************************************************************************************************

-- update customer_review
-- set language_id = (select language_id from language where name = 'German')
-- where film_id = 1

-- update customer_review
-- set language_id = (select language_id from language where name = 'English')
-- where film_id = 4

-- select *
-- from customer_review


-- *******************************************************************************************************
-- 2. Which foreign keys (references) are defined for the customer table? How does this affect the way 
-- in which we INSERT into the customer table?
-- *******************************************************************************************************

-- select *
-- from customer

-- The foreign keys defined in the customer table are:
-- store_id (references the store table)
-- address_id (references the address table)

-- This affects INSERT statements because when inserting a new customer,
-- the values for store_id and address_id must already exist in the referenced tables.
-- Otherwise, the INSERT will fail due to foreign key constraint violation.


-- *******************************************************************************************************
-- 3. We created a new table called customer_review. Drop this table. 
-- Is this an easy step, or does it need extra checking?
-- *******************************************************************************************************

-- drop table if exists customer_review

-- Dropping the table is not always an easy step.
-- Before dropping it, we should check whether other tables
-- have foreign key references to customer_review.
-- If such references exist, PostgreSQL will not allow the table
-- to be dropped unless CASCADE is used.
-- If there are no references, the table can be dropped safely.


-- *******************************************************************************************************
-- 4. Find out how many rentals are still outstanding (ie. have not been returned to the store yet).
-- *******************************************************************************************************

-- select count(*)
-- from rental as r
-- right join inventory as i
-- on i.inventory_id = r.inventory_id
-- where r.return_date is null

-- select count(*)
-- from rental 
-- where return_date is null

-- 183 rentals are still outstanding


-- *********************************************************************************************************
-- 5. Find the 30 most expensive movies which are outstanding (ie. have not been returned to the store yet)
-- *********************************************************************************************************

-- select f.title
-- from rental as r
-- inner join inventory as i on i.inventory_id = r.inventory_id
-- inner join film as f on f.film_id = i.inventory_id
-- where r.return_date is null
-- order by replacement_cost desc
-- limit 30


-- *********************************************************************************************************
-- 6. Your friend is at the store, and decides to rent a movie. He knows he wants to see 4 movies, 
-- but he can’t remember their names. Can you help him find which movies he wants to rent?

-- The 1st film : The film is about a sumo wrestler, and one of the actors is Penelope Monroe.

-- The 2nd film : A short documentary (less than 1 hour long), rated “R”.

-- The 3rd film : A film that his friend Matthew Mahan rented. He paid over $4.00 for the rental, 
-- and he returned it between the 28th of July and the 1st of August, 2005.

-- The 4th film : His friend Matthew Mahan watched this film, as well. It had the word “boat” 
-- in the title or description, and it looked like it was a very expensive DVD to replace.
-- *********************************************************************************************************

-- **1st film** (Park Citizen)

-- select f.title
-- from film as f
-- inner join film_actor as fa on fa.film_id = f.film_id
-- inner join actor as a on a.actor_id = fa.actor_id
-- where f.description ilike '%sumo wrestler%'
-- and a.first_name = 'Penelope' and a.last_name = 'Monroe'

-- **2nd film** (Cupboard Sinners)

-- select f.title
-- from film as f
-- inner join film_category as fc on fc.film_id = f.film_id
-- inner join category as c on c.category_id = fc.category_id
-- where c.name = 'Documentary'
-- and length < 60
-- and rating = 'R'

-- **3d film** (Sugar Wonka)

-- select f.title
-- from film as f
-- inner join inventory as i on i.film_id = f.film_id
-- inner join rental as r on r.inventory_id = i.inventory_id
-- inner join payment as p on p.rental_id = r.rental_id
-- inner join customer as c on c.customer_id = p.customer_id
-- where c.first_name = 'Matthew' and c.last_name = 'Mahan'
-- and p.amount > 4
-- and return_date between '2005-07-28' and '2005-08-01'


-- **4th film**

-- The 4th film : His friend Matthew Mahan watched this film, as well. It had the word “boat” 
-- in the title or description, and it looked like it was a very expensive DVD to replace.

select *
from film as f
inner join inventory as i on i.film_id = f.film_id
inner join rental as r on r.inventory_id = i.inventory_id
inner join payment as p on p.rental_id = r.rental_id
inner join customer as c on c.customer_id = p.customer_id
where c.first_name = 'Matthew' and c.last_name = 'Mahan'
and (f.title ilike '%boat%' or f.description ilike '%boat%')
order by amount desc
limit 1
