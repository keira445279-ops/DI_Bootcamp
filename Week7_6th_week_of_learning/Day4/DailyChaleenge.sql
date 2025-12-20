-- =========================================================
-- Exercise 1: Detailed Medal Analysis
-- =========================================================

-- **********************************************************************************************************************
-- Task 1: Identify competitors who have won at least one medal in events spanning both Summer and Winter Olympics. 
-- Create a temporary table to store these competitors and their medal counts for each season, and then display 
-- the contents of this table.
-- **********************************************************************************************************************

CREATE TEMP TABLE season_participation_with_medals AS
SELECT DISTINCT gc1.person_id, 
COUNT(DISTINCT ce1.event_id) AS winter_medals,
COUNT(DISTINCT ce2.event_id) AS summer_medals
FROM olympics.games_competitor AS gc1
INNER JOIN olympics. games AS g1 ON g1.id = gc1.games_id
INNER JOIN olympics.games_competitor AS gc2 ON gc2.person_id = gc1.person_id
INNER JOIN olympics.games AS g2 ON gc2.games_id = g2.id
INNER JOIN olympics.competitor_event AS ce1 ON ce1.competitor_id = gc1.id
INNER JOINolympics.competitor_event AS ce2 ON ce2.competitor_id = gc2.id
WHERE g1.season = 'Winter' AND ce1.medal_id < 4
AND g2.season = 'Summer' AND ce2.medal_id < 4
GROUP BY gc1.person_id;

SELECT *
FROM season_participation_with_medals;

-- **********************************************************************************************************************
-- Task 2: Create a temporary table to store competitors who have won medals in exactly two different sports, and then 
-- use a subquery to identify the top 3 competitors with the highest total number of medals across all sports. 
-- Display the contents of this table.
-- **********************************************************************************************************************

CREATE TEMP TABLE competitors_two_sports AS
SELECT 
    ce.competitor_id,
    count(distinct s.id) AS sports_count, 
    count(ce.event_id) AS total_medals     
FROM olympics.competitor_event AS ce
INNER JOIN olympics.event AS e ON ce.event_id = e.id
INNER JOIN olympics.sport AS s ON e.sport_id = s.id
WHERE ce.medal_id < 4 
GROUP BY ce.competitor_id
HAVING COUNT(DISTINCT s.id) = 2;

SELECT*
FROM competitors_two_sports
WHERE competitor_id IN (
	SELECT competitor_id
	FROM competitors_two_sports
	ORDER BY total_medals DESC
	LIMIT 3
	)
ORDER BY total_medals DESC 



-- =========================================================
-- Exercise 2: Region and Competitor Performance
-- =========================================================

-- **********************************************************************************************************************
-- Task 1: Retrieve the regions that have competitors who have won the highest number of medals in a single Olympic event. 
-- Use a subquery to determine the event with the highest number of medals for each competitor, and then display 
-- the top 5 regions with the highest total medals.
-- **********************************************************************************************************************

SELECT region_name,
COUNT(*) AS total_top_result
FROM olympics.noc_region AS nr
INNER JOIN olympics.person_region AS pr ON pr.region_id = nr.id
INNER JOIN olympics.games_competitor AS gc ON gc.person_id = pr.person_id
WHERE gc.id IN (
	SELECT competitor_id
	FROM olympics.competitor_event
	WHERE medal_id < 4
	GROUP BY competitor_id, event_id
	ORDER BY COUNT(medal_id) DESC
	LIMIT 100
	)
GROUP BY nr.region_name
ORDER BY COUNT(*) DESC
LIMIT 5


-- **********************************************************************************************************************
-- Task 2: Create a temporary table to store competitors who have participated in more than three Olympic Games but 
-- have not won any medals. Retrieve and display the contents of this table, including their full names and 
-- the number of games they participated in.
-- **********************************************************************************************************************

CREATE TEMP TABLE not_winners_with_three_games AS
SELECT DISTINCT p.full_name, COUNT(DISTINCT gc.games_id) AS games_participated
FROM olympics.person AS p
INNER JOIN olympics.games_competitor AS gc ON gc.person_id = p.id
INNER JOIN olympics.competitor_event AS ce ON ce.competitor_id = gc.id
GROUP BY p.id, p.full_name
HAVING COUNT(DISTINCT gc.games_id) > 3 
AND MIN(ce.medal_id) > 3;

SELECT * 
FROM not_winners_with_three_games;


