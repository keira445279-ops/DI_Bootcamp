
/*
=========================================
Create tables and import csv files
=========================================
*/

CREATE TABLE companies(
company_name VARCHAR(250) PRIMARY KEY,
company_city VARCHAR(100),
company_state VARCHAR(100),
company_type VARCHAR(100),
const_site_category VARCHAR(100)
);

CREATE TABLE functions(
function_code INT PRIMARY KEY,
function VARCHAR(250),
function_group VARCHAR(100)
);

CREATE TABLE employees(
comp_code_emp VARCHAR(50),
employee_code_emp INT PRIMARY KEY,
employee_name_emp VARCHAR (250),
GEN VARCHAR (1),
age INT
);

CREATE TABLE salaries(
comp_code VARCHAR(50),
comp_name VARCHAR(50),
employee_id INT,
employee_name VARCHAR(250),
date TIMESTAMP,
func_code INT,
func VARCHAR(250),
salary TEXT	
);


/*
=========================================
Alter foreign keys
=========================================
*/

ALTER TABLE salaries 
ADD CONSTRAINT fk_comp_name 
FOREIGN KEY (comp_name) REFERENCES companies (company_name);

ALTER TABLE salaries 
ADD CONSTRAINT fk_salaries_employees 
FOREIGN KEY (employee_id) REFERENCES employees (employee_code_emp);

ALTER TABLE salaries 
ADD CONSTRAINT fk_func_code 
FOREIGN KEY (func_code) REFERENCES functions (function_code);

/*
=========================================
Alter salary column
=========================================
*/

ALTER TABLE salaries
ADD COLUMN salary_new NUMERIC (15, 2);

UPDATE salaries
SET salary_new = CAST (REPLACE(salary,',', '.') AS NUMERIC);

ALTER TABLE salaries DROP COLUMN salary;
ALTER TABLE salaries RENAME COLUMN salary_new TO salary;


/*
====================================================================
Exercise 1: Building a Comprehensive Dataset for Employee Analysis
====================================================================
*/

CREATE TEMP TABLE emp_dataset AS(
	select *
	FROM salaries AS s
	LEFT JOIN companies AS c ON c.company_name = s.comp_name
	LEFT JOIN employees AS e ON e.employee_code_emp = s.employee_id
	LEFT JOIN functions AS f ON f.function_code = s.func_code
);

CREATE TABLE df_employee AS
SELECT
	employee_id || '_' || CAST(date AS TEXT) AS id,
	DATE(date) AS month_year,
	employee_id, 
	employee_name, 
	gen AS gender, 
	age, 
	salary, 
	function_group, 
	company_name, 
	company_city, 
	company_state, 
	company_type, 
	const_site_category
FROM emp_dataset;
	


/*
====================================================================
Exercise 2: Cleaning Data for Consistency and Quality
====================================================================
*/

-- 1. run the following SQLite request and observe your new table.

SELECT * 
FROM df_employee;

-- 2. Remove all unwanted spaces from all text columns using TRIM

UPDATE df_employee
SET
	id = TRIM(id),
	employee_name = TRIM(employee_name), 
	gender = TRIM(gender), 
	function_group = TRIM(function_group), 
	company_name = TRIM(company_name), 
	company_city = TRIM(company_city), 
	company_state = TRIM(company_state), 
	company_type = TRIM(company_type), 
	const_site_category = TRIM(const_site_category);


-- 3. Check for NULL values and empty values.

SELECT *
	FROM df_employee
	WHERE id IS NULL
	OR month_year IS NULL
	OR employee_id IS NULL
	OR employee_name IS NULL
	OR gender IS NULL
	OR age IS NULL
	OR salary IS NULL
	OR function_group IS NULL
	OR company_name IS NULL
	OR company_city IS NULL
	OR company_state IS NULL
	OR company_type IS NULL
	OR const_site_category IS NULL;


-- id

SELECT COUNT(id) AS count_missing_id
	FROM df_employee
	WHERE id = ' '
		
-- gender

SELECT COUNT(gender) AS count_missing_gender
	FROM df_employee
	WHERE gender = ' '


-- function_group

SELECT COUNT(function_group) AS count_missing_function_group
	FROM df_employee
	WHERE function_group = ' '

-- company_name

SELECT COUNT(company_name) AS count_missing_company_name
	FROM df_employee
	WHERE company_name = ' '

-- company_city

SELECT COUNT(company_city) AS count_missing_company_city
	FROM df_employee
	WHERE company_city = ' '

-- company_state

SELECT COUNT(company_state) AS count_missing_company_state
	FROM df_employee
	WHERE company_state = ' '

-- company_type

SELECT COUNT(company_type) AS count_missing_company_type
	FROM df_employee
	WHERE company_type = ' '

-- const_site_category

SELECT COUNT(const_site_category) AS count_missing_const_site_category
	FROM df_employee
	WHERE const_site_category = ' '
	   


-- 4. Delete rows of the detected missing values.

-- check the number of rows 
SELECT *
FROM df_employee
WHERE salary IS NULL


DELETE FROM df_employee
WHERE salary IS NULL;

-- check the number of rows 
SELECT *
FROM df_employee
WHERE const_site_category IS NULL

DELETE FROM df_employee
WHERE const_site_category IS NULL;


/*
====================================================================
Exercise 3 : Calculating Current Employee Counts by Company
====================================================================
*/

WITH CurrentMonth AS(
	SELECT MAX(month_year) AS max_month
	FROM df_employee
)
SELECT company_name, month_year AS current_month, COUNT(DISTINCT employee_id) AS number_of_employees
FROM df_employee
WHERE month_year = (SELECT max_month FROM CurrentMonth)
GROUP BY company_name, month_year
ORDER BY number_of_employees DESC;


/*
====================================================================
Exercise 4 : Analyzing Employee Distribution by City and Over Time
====================================================================
*/

-- What is the total number of employees each city? Add a percentage column

WITH EmployeeEveryCity AS(
	SELECT company_city, month_year, COUNT(DISTINCT employee_id) AS count_employee
	FROM df_employee
	GROUP BY company_city, month_year
	ORDER BY company_city, month_year
)
SELECT *, 
	round(
		(count_employee :: numeric / SUM(count_employee) OVER(PARTITION BY company_city)) * 100, 2) AS percentage_employee_per_city
FROM EmployeeEveryCity
ORDER BY company_city, month_year;


-- What is the total number of employees each month?

SELECT month_year, COUNT(DISTINCT employee_id) AS count_employee_in_month
FROM df_employee
GROUP BY month_year
ORDER BY month_year;


-- What is the average number of employees each month?

WITH monthly_count AS(
	SELECT month_year, COUNT(DISTINCT employee_id) AS total_employee
	FROM df_employee
	GROUP BY month_year
)
SELECT 
	 round(AVG(total_employee), 2) AS avg_employees_per_month
FROM monthly_count;


/*
====================================================================
Exercise 5 : Analyzing Employment Trends and Salary Metrics
====================================================================
*/

-- What is the minimum and maximum number of employees throughout all the months? In which months were they?

WITH MonthlyCount AS(
	SELECT month_year, COUNT(DISTINCT employee_id) AS count_employees
	FROM df_employee
	GROUP BY month_year
)
(SELECT 'MAX' AS status, month_year, count_employees
FROM MonthlyCount
ORDER BY count_employees DESC
LIMIT 1)
UNION ALL
(SELECT 'MIN' AS status, month_year, count_employees
FROM MonthlyCount
ORDER BY count_employees 
LIMIT 1);


-- What is the monthly average number of employees by function group?

WITH monthly_function_counts AS (
	SELECT function_group, 
	month_year, 
	COUNT(DISTINCT employee_id) AS employee_count
FROM df_employee
GROUP BY function_group, month_year
)
SELECT function_group, 
	round(AVG(employee_count), 2) AS avg_monthle_employee
FROM monthly_function_counts
GROUP BY function_group
ORDER BY avg_monthle_employee DESC;


-- What is the annual average salary?

SELECT
	EXTRACT(YEAR FROM month_year) AS salary_year,
	round(AVG(salary), 2) AS annual_avg_salary
FROM df_employee
GROUP BY salary_year
ORDER BY salary_year
