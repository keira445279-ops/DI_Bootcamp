-- Create the employees table
CREATE TABLE employees (
    employee_id INT PRIMARY KEY,
    employee_name VARCHAR(50),
    salary DECIMAL(10, 2),
    hire_date VARCHAR(20),
    department VARCHAR(50)
);

-- Insert 20 sample records 
INSERT INTO employees (employee_id, employee_name, salary, hire_date, department) VALUES
(1, 'Amy West', 60000.00, '2021-01-15', 'HR'),
(2, 'Ivy Lee', 75000.50, '2020-05-22', 'Sales'),
(3, 'joe smith', 80000.75, '2019-08-10', 'Marketing'), 
(4, 'John White', 90000.00, '2020-11-05', 'Finance'),
(5, 'Jane Hill', 55000.25, '2022-02-28', 'IT'),
(6, 'Dave West', 72000.00, '2020-03-12', 'Marketing'),
(7, 'Fanny Lee', 85000.50, '2018-06-25', 'Sales'),
(8, 'Amy Smith', 95000.25, '2019-11-30', 'Finance'),
(9, 'Ivy Hill', 62000.75, '2021-07-18', 'IT'),
(10, 'Joe White', 78000.00, '2022-04-05', 'Marketing'),
(11, 'John Lee', 68000.50, '2018-12-10', 'HR'),
(12, 'Jane West', 89000.25, '2017-09-15', 'Sales'),
(13, 'Dave Smith', 60000.75, '2022-01-08', NULL),
(14, 'Fanny White', 72000.00, '2019-04-22', 'IT'),
(15, 'Amy Hill', 84000.50, '2020-08-17', 'Marketing'),
(16, 'Ivy West', 92000.25, '2021-02-03', 'Finance'),
(17, 'Joe Lee', 58000.75, '2018-05-28', 'IT'),
(18, 'John Smith', 77000.00, '2019-10-10', 'HR'),
(19, 'Jane Hill', 81000.50, '2022-03-15', 'Sales'),
(20, 'Dave White', 70000.25, '2017-12-20', 'Marketing');


-- ===========================================
-- 1. Identify and handle any missing value.
-- ===========================================

-- for employee_id 
SELECT *
FROM employees
WHERE employee_id IS NULL;

-- for employee_name
SELECT *
FROM employees
WHERE employee_name IS NULL;

-- for salary
SELECT *
FROM employees
WHERE salary IS NULL;


-- for hire_date
SELECT *
FROM employees
WHERE hire_date IS NULL;

-- for department
SELECT *
FROM employees
WHERE department IS NULL;

UPDATE employees
SET department = 'default_value'
WHERE department IS NULL;


-- ===============================================================
-- 2. Check for and eliminate any duplicate rows in the dataset.
-- ===============================================================

SELECT employee_id, employee_name, salary, hire_date, department, COUNT(*)
FROM employees
GROUP BY employee_id, employee_name, salary, hire_date, department
HAVING COUNT(*) > 1;


-- ==================================================================================================
-- 3. Correct any structural issues, such as inconsistent naming conventions or formatting errors.
-- ==================================================================================================

UPDATE employees
SET employee_name = 'Joe Smith'
WHERE employee_name = 'First Last';


-- ==================================================================================================
-- 4. Ensure all columns have appropriate data types (e.g. the hire_date column).
-- ==================================================================================================

ALTER TABLE employees
ALTER COLUMN hire_date TYPE DATE
USING hire_date::DATE;


-- ==================================================================================================
-- 5. Detect and address any outliers that may skew the analysis.
-- ==================================================================================================

SELECT *
FROM (
	select *, 
		AVG(salary) OVER() AS avg_salary, 
		STDDEV(salary) OVER() AS std_salary
	from employees
) AS sub
WHERE salary > (avg_salary + 2 * std_salary)
OR salary < (avg_salary - 2 * std_salary);


SELECT * 
FROM employees 
WHERE department IS NULL OR salary IS NULL;


SELECT COALESCE(department, 'default_value') as department, AVG(salary)
FROM employees
GROUP BY 1;


-- ==================================================================================================
-- 6. Standardize and normalize data where applicable to ensure consistency.
-- ==================================================================================================

UPDATE employees
SET 
    employee_name = INITCAP(TRIM(employee_name)),
    department = UPPER(TRIM(department));

