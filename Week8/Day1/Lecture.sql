-- ==========================================================
-- Defying missing values and fill them
-- ==========================================================

CREATE TABLE sample_data (id INT, value INT);
INSERT INTO sample_data (id, value) VALUES (1, 10), (2, NULL), (3, 30);

select *
from sample_data
where value is null

update sample_data
set value = (select avg(value) from sample_data)
where value is null


CREATE TABLE sample_data2 (id INT, value INT);
INSERT INTO sample_data2 (id, value) VALUES (1, 10), (2, NULL), (3, 30);

SELECT COALESCE(value, 20) FROM sample_data2

CREATE TABLE sample_data3 (id INT, value INT);
INSERT INTO sample_data3 (id, value) VALUES (1, 10), (2, NULL), (3, 30);

SELECT COALESCE(value, (select round(avg(value)) from sample_data3)) FROM sample_data3



-- Detect
SELECT *
FROM sample_data WHERE value IS NULL;
-- Replace with default (e.g., 0)
SELECT id, COALESCE(value, 0) AS cleaned_value
FROM sample_data;
SELECT id, COALESCE(value, (SELECT ROUND(AVG(value)) FROM sample_data)) AS cleaned_value
FROM sample_data;
--Update
UPDATE sample_data
SET value = (SELECT AVG(value)
			 FROM sample_data WHERE value IS NOT NULL)
WHERE value IS NULL;

select count(*)
from sample_data 
where value in null


-- ==========================================================
-- Removing Duplicates
-- ==========================================================

CREATE TABLE sample_data4 (id INT, value INT);
INSERT INTO sample_data4 (id, value) VALUES (1, 10), (2, 20), (3, 10), (3,10), (4,10);

select value, count(*)
from sample_data4
group by value
having count(*) > 1

select id, value, count(*)
from sample_data4
group by id, value
having count(*) > 1


WITH ranked AS (
    SELECT
        id,
        value,
        ROW_NUMBER() OVER (PARTITION BY id, value ORDER BY id) AS rn
    FROM sample_data4
)
DELETE FROM sample_data4 sd
USING ranked r
WHERE sd.id = r.id
  AND sd.value = r.value
  AND r.rn > 1;


select * from sample_data4


-- ==========================================================
-- Correcting Inconsistent Data
-- ==========================================================

CREATE TABLE sample_data5 (id INT, value VARCHAR(50));
INSERT INTO sample_data5 (id, value) VALUES (1, 'apple'), (2, 'Apple'), (3, 'APPLE');

select lower (value) from sample_data5

update sample_data5
set value = 'Apple'
where value in ('apple', 'APPLE');

select *
from sample_data5