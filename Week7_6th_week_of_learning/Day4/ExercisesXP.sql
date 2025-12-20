-- =======================================
-- Exercise 1: Complex Subquery Analysis
-- =======================================

-- **********************************************************************************************************************
-- Task 1: Find the average age of competitors who have won at least one medal, grouped by the type of medal they won. 
-- Use a correlated subquery to achieve this.
-- **********************************************************************************************************************

SELECT m.medal_name, 
(
SELECT round(AVG (age),2)
FROM olympics.games_competitor AS gc
INNER JOIN olympics.competitor_event AS ce ON ce.competitor_id = gc.id
WHERE ce.medal_id = m.id
) AS av_age
FROM olympics.medal AS m
WHERE m.medal_name != 'NA';


-- **********************************************************************************************************************
-- Task 2: Identify the top 5 regions with the highest number of unique competitors who have participated in 
-- more than 3 different events. Use nested subqueries to filter and aggregate the data.
-- **********************************************************************************************************************

SELECT 
    nr.region_name, 
    COUNT(DISTINCT gc.id) AS unique_competitors
FROM olympics.noc_region AS nr
JOIN olympics.person_region AS pr ON nr.id = pr.region_id
JOIN olympics.games_competitor AS gc ON pr.person_id = gc.person_id
WHERE gc.id IN (
    SELECT competitor_id
	FROM olympics.competitor_event
	GROUP BY competitor_id
	HAVING COUNT(DISTINCT event_id) > 3
)
GROUP BY nr.region_name
ORDER BY unique_competitors DESC
LIMIT 5;


-- **********************************************************************************************************************
-- Task 3: Create a temporary table to store the total number of medals won by each competitor and filter 
-- to show only those who have won more than 2 medals. Use subqueries to aggregate the data.
-- **********************************************************************************************************************

CREATE TEMP TABLE top_medalists AS 
SELECT 
    p.full_name, 
    agg.total_medals
FROM (
    SELECT competitor_id, COUNT(medal_id) AS total_medals
	FROM olympics.competitor_event
	WHERE medal_id != 4
	GROUP BY competitor_id
	HAVING COUNT(medal_id) > 2
) AS agg
INNER JOIN olympics.games_competitor gc ON gc.id = agg.competitor_id
INNER JOIN olympics.person p ON p.id = gc.person_id
ORDER BY agg.total_medals DESC;

SELECT *
FROM top_medalists

-- **********************************************************************************************************************
-- Task 4: Use a subquery within a DELETE statement to remove records of competitors who have not won any medals 
-- from a temporary table created for analysis.
-- **********************************************************************************************************************

CREATE TEMP TABLE COMPETITOR_ANALYSIS AS 
SELECT id, person_id FROM olympics.games_competitor;

DELETE FROM COMPETITOR_ANALYSIS
WHERE ID NOT IN (
	SELECT competitor_id
	FROM olympics.competitor_event AS ce
	INNER JOIN olympics.medal AS m ON m.id = ce.medal_id
	WHERE m.medal_name != 'NA'
	AND ce.competitor_id IS NOT NULL
	);


SELECT *
FROM COMPETITOR_ANALYSIS




-- =========================================================
-- Exercise 2: Advanced Data Manipulation and Optimization
-- =========================================================

-- **********************************************************************************************************************
-- Task 1: Update the heights of competitors based on the average height of competitors from the same region. 
-- Use a correlated subquery within the UPDATE statement.
-- **********************************************************************************************************************

UPDATE olympics.person
SET height = (
	SELECT AVG(p2.height) 
	FROM olympics.person AS p2
	INNER JOIN olympics.person_region AS pr2 ON pr2.person_id = p2.id
	WHERE pr2.region_id = (
		SELECT pr.region_id 
		FROM olympics.person_region AS pr
		WHERE pr.person_id = p2.id
		)
	)
WHERE height IS NULL


-- **********************************************************************************************************************
-- Task 2: Insert new records into a temporary table for competitors who participated in more than one event 
-- in the same games and list their total number of events participated. Use nested subqueries for filtering.
-- **********************************************************************************************************************

CREATE TEMP TABLE multi_event_competitors(
	competitor_id int,
	total_events int
)

INSERT INTO multi_event_competitors (competitor_id, total_events) 
SELECT
	ce.competitor_id, 
	COUNT(event_id) AS total_events
FROM olympics.competitor_event AS ce
WHERE ce.competitor_id IN (
	SELECT ce_inner.competitor_id 
	FROM olympics.competitor_event AS ce_inner
	INNER JOIN olympics.games_competitor AS gc 
	ON gc.id = ce_inner.competitor_id 
	GROUP BY ce_inner.competitor_id, gc.games_id 
	HAVING COUNT(ce_inner.event_id) > 1
	)
GROUP BY ce.competitor_id


SELECT *
FROM multi_event_competitors


-- **********************************************************************************************************************
-- Task 3: Identify regions where the average number of medals won per competitor is greater than the overall average. 
-- Use subqueries to calculate and compare averages.
-- **********************************************************************************************************************

SELECT region_name, 
round(AVG(sub_region.medal_per_person), 2) AS region_average
FROM olympics.noc_region AS nr
INNER JOIN olympics.person_region AS pr ON pr.region_id = nr.id
INNER JOIN olympics.games_competitor AS gc ON gc.person_id = pr.person_id
INNER JOIN(
		SELECT competitor_id, COUNT(medal_id) AS medal_per_person
		FROM olympics.competitor_event
		WHERE medal_id != 4
		GROUP BY competitor_id
		) AS sub_region ON sub_region.competitor_id = gc.id
GROUP BY nr.region_name
HAVING AVG(sub_region.medal_per_person) > (
	SELECT round(AVG(medal_per_person), 2) AS total_average
	FROM (
		SELECT competitor_id, COUNT(medal_id) AS medal_per_person
		FROM olympics.competitor_event
		WHERE medal_id != 4
		GROUP BY competitor_id
		) AS sub)
ORDER BY region_average 

-- **********************************************************************************************************************
-- Task 4: Create a temporary table to track competitors’ participation across different seasons and identify 
-- those who have participated in both Summer and Winter games.
-- **********************************************************************************************************************

CREATE TEMP TABLE season_participation AS
SELECT DISTINCT gc1.person_id
FROM olympics.games_competitor AS gc1
INNER JOIN olympics. games AS g1 ON g1.id = gc1.games_id
INNER JOIN olympics.games_competitor AS gc2 ON gc2.person_id = gc1.person_id
INNER JOIN olympics.games AS g2 ON gc2.games_id = g2.id
WHERE g1.season = 'Winter' 
AND g2.season = 'Summer';

SELECT *
FROM season_participation


