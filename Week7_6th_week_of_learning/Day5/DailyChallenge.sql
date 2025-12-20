
-- **********************************************************************************************************
-- Task 1: Calculate the Average Budget Growth Rate for Each Production Company
-- Calculate the average budget growth rate for each production company across all movies they have produced. 
-- Use window functions to determine the budget growth rate and then calculate the average growth rate.
-- **********************************************************************************************************

WITH BudgetGrowthRate AS (
	SELECT 
	pc.company_name, 
	m.title,
	m.budget AS budget_per_film,
	LAG(m.budget, 1) OVER (PARTITION BY pc.company_name ORDER BY m.release_date) AS previous_budget
	FROM movies.movie AS m 
	INNER JOIN movies.movie_company AS mc ON mc.movie_id = m.movie_id
	INNER JOIN movies.production_company AS pc ON pc.company_id = mc.company_id
	WHERE m.budget > 0
	)
SELECT
	company_name, 	
	round(AVG((budget_per_film - previous_budget) * 1.0 / previous_budget), 2) AS average_grith_rate
FROM BudgetGrowthRate
WHERE previous_budget IS NOT NULL
GROUP BY company_name
ORDER BY average_grith_rate DESC



-- **********************************************************************************************************
-- Task 2: Determine the Most Consistently High-Rated Actor
-- Identify the actor who has appeared in the most movies that are rated above the average rating of all movies. 
-- Use window functions and CTEs to calculate the average rating and filter the actors based on this criterion.
-- **********************************************************************************************************

WITH MostHighRatedActor AS (
	SELECT m.*,
	p.person_name, 
	AVG(m.vote_average) OVER () AS total_average_rating
	FROM movies.movie AS m
	INNER JOIN  movies.movie_cast AS mc ON mc.movie_id = m.movie_id
	INNER JOIN movies.person AS p ON p.person_id = mc.person_id
	),
	HighRatedMovie AS(
		SELECT person_name
		FROM MostHighRatedActor
		WHERE vote_average > total_average_rating
		)
SELECT person_name,
COUNT(*) AS high_rated_movie
FROM HighRatedMovie
GROUP BY person_name
ORDER BY high_rated_movie DESC
limit 1


		
-- **********************************************************************************************************
-- Task 3: Calculate the Rolling Average Revenue for Each Genre
-- Calculate the rolling average revenue for movies within each genre, considering only the last three 
-- movies released in the genre. Use window functions with the ROWS frame specification to achieve this.
-- **********************************************************************************************************


select g.genre_name,
	m.title,
	m.release_date,
	m.revenue,
	AVG(m.revenue) OVER (PARTITION BY g.genre_name ORDER BY m.release_date ROWS BETWEEN 2 PRECEDING AND CURRENT ROW) AS rolling_avg_revenue
FROM movies.movie AS m
INNER JOIN movies.movie_genres AS mg ON mg.movie_id = m.movie_id
INNER JOIN movies.genre AS g ON g.genre_id = mg.genre_id
WHERE m.revenue > 0 
ORDER BY g.genre_name, m.release_date DESC



-- **********************************************************************************************************
-- Task 4: Identify the Highest-Grossing Movie Series
-- Identify the movie series (based on shared keywords) with the highest total revenue. 
-- Use window functions and CTEs to group movies by their series and calculate the total revenue.
-- **********************************************************************************************************

WITH HighestGrossingMovieSeries AS (
	SELECT
		TRIM(SPLIT_PART(REPLACE(REPLACE(title, ' and ', ':'), ',', ':'), ':', 1)) AS movie_series,
		SUM (revenue) AS total_revenue,
		COUNT(*) AS movie_count,
		round(AVG(revenue)) AS avg_revenue_per_movie
	FROM movies.movie 
	WHERE revenue > 0
	GROUP BY movie_series
	-- group by 1 -- the 1st column in select 
	HAVING COUNT(*) > 1
)
select *
FROM HighestGrossingMovieSeries
ORDER BY total_revenue DESC
-- LIMIT 20
