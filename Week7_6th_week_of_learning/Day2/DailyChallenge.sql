-- CREATE TABLE FirstTab (
--      id integer, 
--      name VARCHAR(10)
-- )

-- INSERT INTO FirstTab VALUES
-- (5,'Pawan'),
-- (6,'Sharlee'),
-- (7,'Krish'),
-- (NULL,'Avtaar')

-- SELECT * FROM FirstTab

-- CREATE TABLE SecondTab (
--     id integer 
-- )

-- INSERT INTO SecondTab VALUES
-- (5),
-- (NULL)


-- SELECT * FROM SecondTab


-- =========================================================
-- Q1. What will be the OUTPUT of the following statement?
-- =========================================================

-- SELECT COUNT(*) 
--     FROM FirstTab AS ft WHERE ft.id NOT IN ( SELECT id FROM SecondTab WHERE id IS NULL )

-- The output will be 0
-- Because SQL always returns False in statement NOT IN(NULL), because NULL IS UNKNOWN for sql


-- =========================================================
-- Q2. What will be the OUTPUT of the following statement?
-- =========================================================

    -- SELECT COUNT(*) 
    -- FROM FirstTab AS ft WHERE ft.id NOT IN ( SELECT id FROM SecondTab WHERE id = 5 )

-- The output will be 2
-- Because the query asks us not include in count person with id 5, so this person will be excluded
-- NULL is unknown for SQL and will be excluded too
-- So only two persons will stay with id 6 and 7


-- =========================================================
-- Q3. What will be the OUTPUT of the following statement?
-- =========================================================

-- SELECT COUNT(*) 
--     FROM FirstTab AS ft WHERE ft.id NOT IN ( SELECT id FROM SecondTab )

-- The output will be 0
-- Because there is a NULL in condition 'where' and all id in first table will be compared with NOT IN (5, NULL)
-- As NULL is unknown for SQL, the iutput will be 0


-- =========================================================
-- Q4. What will be the OUTPUT of the following statement?
-- =========================================================

    -- SELECT COUNT(*) 
    -- FROM FirstTab AS ft WHERE ft.id NOT IN ( SELECT id FROM SecondTab WHERE id IS NOT NULL )

-- The output will be 2
-- Because the query asks us not include in count person with NOT NULL ID, that is 5, so this person will be excluded
-- NULL is unknown for SQL and will be excluded too
-- So only two persons will stay with id 6 and 7
	
	