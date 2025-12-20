-- =================================================================
-- Exercise 1: Movie Rankings and Analysis
-- =================================================================

-- ******************************************************************************
-- Task 1: Rank Movies by Popularity within Each Genre
-- Use the RANK() function to rank movies by their popularity within each genre. 
-- Display the genre name, movie title, and their rank based on popularity.
-- ******************************************************************************

SELECT m.title, g.genre_name, m.popularity,
	RANK() OVER(PARTITION BY g.genre_name ORDER BY m.popularity DESC) AS rank_movies_by_popularity
FROM movies.movie as m
INNER JOIN movies.movie_genres AS mg ON mg.movie_id = m.movie_id
INNER JOIN movies.genre AS g ON g.genre_id = mg.genre_id


-- **********************************************************************************************************
-- Task 2: Identify the Top 3 Movies by Revenue within Each Production Company
-- Use the NTILE() function to divide the movies produced by each production 
-- company into quartiles based on revenue. Display the company name, movie title, revenue, and quartile.
-- **********************************************************************************************************

SELECT *
FROM (
	SELECT pc.company_name, m.title, m.revenue,
		NTILE(4) OVER (PARTITION BY pc.company_name ORDER BY m.revenue DESC) AS revenue_qurtile
	FROM movies.movie AS m
	INNER JOIN movies.movie_company AS mc ON mc.movie_id = m.movie_id
	INNER JOIN movies.production_company AS pc ON pc.company_id = mc.company_id
	) AS t1
WHERE revenue_qurtile = 1


-- **********************************************************************************************************
-- Task 3: Calculate the Running Total of Movie Budgets for Each Genre
-- Use the SUM() function with the ROWS frame specification to calculate the running total of movie budgets 
-- within each genre. Display the genre name, movie title, budget, and running total budget.
-- **********************************************************************************************************

SELECT g.genre_name, m.title, m.budget,
	SUM(m.budget) OVER (PARTITION BY g.genre_name ORDER BY m.title ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW) AS run_total_budgets
FROM movies.movie AS m
INNER JOIN movies.movie_genres AS mg ON mg.movie_id = m.movie_id
INNER JOIN movies.genre AS g ON g.genre_id = mg.genre_id



-- **********************************************************************************************************
-- Task 4: Identify the Most Recent Movie for Each Genre
-- Use the FIRST_VALUE() function to find the most recent movie within each genre based on the release date. 
-- Display the genre name, movie title, and release date.
-- **********************************************************************************************************

SELECT DISTINCT g.genre_name, 
	FIRST_VALUE(m.title) OVER (PARTITION BY g.genre_name ORDER BY m.release_date DESC) AS most_recent_movie,
	FIRST_VALUE(m.release_date) OVER (PARTITION BY g.genre_name ORDER BY m.release_date DESC) AS released_date
FROM movies.movie AS m
INNER JOIN movies.movie_genres AS mg ON mg.movie_id = m.movie_id
INNER JOIN movies.genre AS g ON g.genre_id = mg.genre_id
ORDER BY g.genre_name




-- =================================================================
-- Exercise 2: Cast and Crew Performance Analysis
-- =================================================================

-- **********************************************************************************************************
-- Task 1: Rank Actors by Their Appearance in Movies
-- Use the DENSE_RANK() function to rank actors based on the number of movies they have appeared in. 
-- Display the actor’s name and their rank.
-- **********************************************************************************************************

SELECT p.person_name, 
	   COUNT(mc.movie_id) AS movie_count, 
	   DENSE_RANK() OVER (ORDER BY COUNT(mc.movie_id) DESC) AS rank_actor
FROM movies.movie as m 
INNER JOIN  movies.movie_cast AS mc ON mc.movie_id = m.movie_id
INNER JOIN movies.person AS p ON p.person_id = mc.person_id
GROUP BY p.person_name


-- **********************************************************************************************************
-- Task 2: Identify the Top Director by Average Movie Rating
-- Use a CTE and the RANK() function to find the director with the highest average movie rating. 
-- Display the director’s name and their average rating.
-- **********************************************************************************************************

WITH DirectorMovieAverageRating AS (
	SELECT 
		p.person_name,
		AVG (m.vote_average) AS avg_rating
	FROM movies.movie AS m
	INNER JOIN movies.movie_crew AS mc on mc.movie_id = m.movie_id
	INNER JOIN movies.person AS p on p.person_id = mc.person_id
	where mc.job = 'Director'
	GROUP BY p.person_name
)
SELECT 
	person_name,
	ROUND(avg_rating, 2) AS average_rating,
	RANK() OVER (ORDER BY avg_rating DESC) AS director_rank
FROM DirectorMovieAverageRating
ORDER BY director_rank 



-- **********************************************************************************************************
-- Task 3: Calculate the Cumulative Revenue of Movies Acted by Each Actor
-- Use the SUM() function to calculate the cumulative revenue of movies acted by each actor. 
-- Display the actor’s name and the cumulative revenue.
-- **********************************************************************************************************

WITH ActorCumulativeRevenue AS (
	SELECT 
		p.person_name,
		SUM(m.revenue) AS total_revenue
	FROM movies.movie AS m
	INNER JOIN  movies.movie_cast AS mc ON mc.movie_id = m.movie_id
	INNER JOIN movies.person AS p ON p.person_id = mc.person_id
	GROUP BY p.person_name
)
SELECT 
	person_name,
	ROUND(total_revenue) AS total_revenue1,
	SUM(total_revenue) OVER (ORDER BY total_revenue DESC) AS cumulative_revenue
FROM ActorCumulativeRevenue
ORDER BY total_revenue DESC



-- **********************************************************************************************************
-- Task 4: Identify the Director Whose Movies Have the Highest Total Budget
-- Use a CTE and a window function to find the director whose movies have the highest total budget. 
-- Display the director’s name and the total budget.
-- **********************************************************************************************************

WITH DirectorTotalBudget AS (
	SELECT 
		p.person_name,
		SUM (m.budget) AS total_budget
	FROM movies.movie AS m
	INNER JOIN movies.movie_crew AS mc ON mc.movie_id = m.movie_id
	INNER JOIN movies.person AS p on p.person_id = mc.person_id
	where mc.job = 'Director'
	GROUP BY p.person_name
)
SELECT 
	person_name,
	ROUND(total_budget) AS total_budget1,
	DENSE_RANK() OVER (ORDER BY total_budget DESC) AS rank_movies_budget
FROM DirectorTotalBudget
ORDER BY total_budget desc







