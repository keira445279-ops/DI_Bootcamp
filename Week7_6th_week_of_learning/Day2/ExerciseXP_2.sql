-- ************************************************************************************************
-- 1. In the dvdrental database write a query to select all the columns from the “customer” table.
-- ************************************************************************************************
-- SELECT
-- 	*
-- FROM
-- 	CUSTOMER

-- ************************************************************************************************
-- 2. Write a query to display the names (first_name, last_name) using an alias named “full_name”.
-- ************************************************************************************************
-- SELECT
-- 	FIRST_NAME || ' ' || LAST_NAME AS FULL_NAME
-- FROM
-- 	CUSTOMER

-- ************************************************************************************************
-- 3. Lets get all the dates that accounts were created. Write a query to select all 
-- the create_date from the “customer” table (there should be no duplicates).
-- ************************************************************************************************
-- SELECT DISTINCT
-- 	CREATE_DATE
-- FROM
-- 	CUSTOMER

-- ************************************************************************************************
-- 4. Write a query to get all the customer details from the customer table, it should 
-- be displayed in descending order by their first name.
-- ************************************************************************************************
-- SELECT
-- 	*
-- FROM
-- 	CUSTOMER
-- ORDER BY
-- 	FIRST_NAME DESC

-- ************************************************************************************************
-- 5. Write a query to get the film ID, title, description, year of release and rental rate in 
-- ascending order according to their rental rate.
-- ************************************************************************************************
-- SELECT
-- 	FILM_ID,
-- 	TITLE,
-- 	DESCRIPTION,
-- 	RELEASE_YEAR,
-- 	RENTAL_RATE
-- FROM
-- 	FILM
-- ORDER BY
-- 	RENTAL_RATE

-- ************************************************************************************************
-- 6. Write a query to get the address, and the phone number of all customers living 
-- in the Texas district, these details can be found in the “address” table.
-- ************************************************************************************************
-- SELECT
-- 	ADDRESS,
-- 	PHONE
-- FROM
-- 	ADDRESS
-- WHERE
-- 	DISTRICT = 'Texas'

-- ************************************************************************************************
-- 7. Write a query to retrieve all movie details where the movie id is either 15 or 150.
-- ************************************************************************************************
-- SELECT
-- 	*
-- FROM
-- 	FILM
-- WHERE
-- 	FILM_ID BETWEEN 15 AND 150

-- ************************************************************************************************
-- 8. Write a query which should check if your favorite movie exists in the database. 
-- Have your query get the film ID, title, description, length and the rental rate, 
-- these details can be found in the “film” table.
-- ************************************************************************************************
-- SELECT
-- 	FILM_ID,
-- 	TITLE,
-- 	DESCRIPTION,
-- 	FILM.LENGTH,
-- 	RENTAL_RATE
-- FROM
-- 	FILM
-- WHERE
-- 	TITLE = 'Angels Life'
-- 	OR TITLE = 'Casablanca'

-- Angels Lifi is in the base and Casablanca is not in the base


-- ************************************************************************************************
-- 9. No luck finding your movie? Maybe you made a mistake spelling the name. 
-- Write a query to get the film ID, title, description, length and the rental rate of all 
-- the movies starting with the two first letters of your favorite movie.
-- ************************************************************************************************
-- SELECT
-- 	FILM_ID,
-- 	TITLE,
-- 	DESCRIPTION,
-- 	FILM.LENGTH,
-- 	RENTAL_RATE
-- FROM
-- 	FILM
-- WHERE
-- 	TITLE ILIKE 'CA%'


-- ************************************************************************************************
-- 10. Write a query which will find the 10 cheapest movies.
-- ************************************************************************************************
-- SELECT
-- 	*
-- FROM
-- 	FILM
-- ORDER BY
-- 	REPLACEMENT_COST
-- LIMIT
-- 	10


-- ************************************************************************************************
-- 11. Not satisfied with the results. Write a query which will find the next 10 cheapest movies.
-- Bonus: Try to not use LIMIT.
-- ************************************************************************************************
-- SELECT
-- 	*
-- FROM
-- 	(
-- 		SELECT
-- 			*,
-- 			ROW_NUMBER() OVER (
-- 				ORDER BY
-- 					REPLACEMENT_COST
-- 			) AS RN
-- 		FROM
-- 			FILM
-- 	) SUB
-- WHERE
-- 	RN BETWEEN 11 AND 20


-- ************************************************************************************************
-- 12. Write a query which will join the data in the customer table and the payment table. 
-- You want to get the first name and last name from the curstomer table, as well as the amount 
-- and the date of every payment made by a customer, ordered by their id (from 1 to…).
-- ************************************************************************************************
-- SELECT
-- 	C.FIRST_NAME,
-- 	C.LAST_NAME,
-- 	P.AMOUNT,
-- 	P.PAYMENT_DATE
-- FROM
-- 	CUSTOMER AS C
-- 	INNER JOIN PAYMENT AS P ON P.CUSTOMER_ID = C.CUSTOMER_ID
-- ORDER BY
-- 	C.CUSTOMER_ID


-- ************************************************************************************************
-- 13. You need to check your inventory. Write a query to get all the movies which 
-- are not in inventory.
-- ************************************************************************************************
-- SELECT
-- 	F.*
-- FROM
-- 	FILM AS F
-- 	LEFT JOIN INVENTORY AS I ON F.FILM_ID = I.FILM_ID
-- WHERE
-- 	I.FILM_ID IS NULL

-- ************************************************************************************************
-- 14. Write a query to find which city is in which country.
-- ************************************************************************************************
-- SELECT
-- 	CITY.CITY,
-- 	COUNTRY.COUNTRY
-- FROM
-- 	CITY
-- 	INNER JOIN COUNTRY ON COUNTRY.COUNTRY_ID = CITY.COUNTRY_ID
-- ORDER BY
-- 	COUNTRY

-- ************************************************************************************************
-- 15. Bonus You want to be able to see how your sellers have been doing? Write a query to get 
-- the customer’s id, names (first and last), the amount and the date of payment ordered by the 
-- id of the staff member who sold them the dvd.
-- ************************************************************************************************

-- SELECT
-- 	S.STAFF_ID,
-- 	C.CUSTOMER_ID,
-- 	C.FIRST_NAME,
-- 	C.LAST_NAME,
-- 	P.AMOUNT,
-- 	P.PAYMENT_DATE
-- FROM
-- 	STAFF AS S
-- 	INNER JOIN PAYMENT AS P ON P.STAFF_ID = S.STAFF_ID
-- 	INNER JOIN CUSTOMER AS C ON C.CUSTOMER_ID = P.CUSTOMER_ID
-- ORDER BY
-- 	S.STAFF_ID







