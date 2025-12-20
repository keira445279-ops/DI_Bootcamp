CREATE TABLE employees_new (
    employee_id INT PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    department_id INT,
    salary DECIMAL(10, 2)
);
CREATE TABLE sales_data (
    sale_id INT PRIMARY KEY,
    employee_id INT,
    sales DECIMAL(10, 2),
    FOREIGN KEY (employee_id) REFERENCES employees_new(employee_id)
);
INSERT INTO employees_new (employee_id, first_name, last_name, department_id, salary) VALUES
(1, 'John', 'Doe', 1, 60000),
(2, 'Jane', 'Smith', 2, 80000),
(3, 'Jim', 'Brown', 3, 90000),
(4, 'Jake', 'White', 4, 70000),
(5, 'Jill', 'Green', 5, 75000),
(6, 'Jack', 'Black', 3, 95000),
(7, 'Jerry', 'Gray', 2, 82000),
(8, 'Jim', 'Black', 3, 90000),
(9, 'Julia', 'Smith', 2, 80000);
INSERT INTO sales_data (sale_id, employee_id, sales) VALUES
(1, 1, 1000),
(2, 2, 1500),
(3, 3, 2000),
(4, 4, 700),
(5, 5, 1300),
(6, 6, 1750),
(7, 7, 1200),
(8, 8, 2000),
(9, 9, 1200);


CREATE TABLE employees (
    department_id INT,
    employee_id INT,
    salary INT
);
INSERT INTO employees (department_id, employee_id, salary) VALUES
(1, 101, 80000),
(1, 102, 75000),
(1, 103, 75000),
(1, 104, 60000),
(2, 201, 90000),
(2, 202, 90000),
(2, 203, 85000),
(2, 204, 80000);



select department_id, employee_id, salary,
	row_number() over (partition by department_id order by salary) as row_number,
	rank() over (partition by department_id order by salary) as row_number,
	dense_rank() over (partition by department_id order by salary) as row_number
from employees;


SELECT department_id, employee_id, salary,
       NTILE(3) OVER (PARTITION BY department_id ORDER BY salary DESC) AS quartile
FROM employees;


SELECT e.employee_id, e.first_name, e.last_name, e.department_id, s.sales,
       MIN(s.sales) OVER (PARTITION BY e.department_id ORDER BY e.salary) AS sum_by_department
FROM employees_new e
JOIN sales_data s ON e.employee_id = s.employee_id;


SELECT e.employee_id, e.first_name, e.last_name, e.department_id, s.sales,
       COUNT(e.employee_id) OVER (PARTITION BY e.department_id) AS employees_by_department
FROM employees_new e
JOIN sales_data s ON e.employee_id = s.employee_id;


SELECT e.employee_id, e.first_name, e.last_name, e.department_id, s.sales,
       AVG(salary) OVER (ORDER BY salary) AS run_avg
FROM employees_new e
JOIN sales_data s ON e.employee_id = s.employee_id;

SELECT e.employee_id, e.first_name, e.last_name, e.department_id, s.sales,salary,
       SUM(salary) OVER (ORDER BY salary) AS run_sum
FROM employees_new e
JOIN sales_data s ON e.employee_id = s.employee_id;


SELECT e.employee_id, e.first_name, e.last_name, e.department_id, salary,
       SUM(salary) OVER (PARTITION BY e.department_id) AS sum_salary_by_department
FROM employees_new e
JOIN sales_data s ON e.employee_id = s.employee_id;


SELECT e.first_name, e.last_name, e.department_id, s.sales,
	DENSE_RANK() OVER(PARTITION BY e.department_id ORDER BY s.sales desc) AS sales_rank
FROM employees_new e
JOIN sales_data s ON e.employee_id = s.employee_id;


SELECT e.first_name, e.last_name, e.department_id, s.sales,
	SUM(s.sales) OVER (PARTITION BY e.employee_id) AS total_sales_for_employee,
	SUM(s.sales) OVER (ORDER BY e.employee_id) AS run_total_sum
FROM employees_new e
JOIN sales_data s ON e.employee_id = s.employee_id;


-- Create the employees table with a consistent employee_id and an additional month column
CREATE TABLE employees_history (
    employee_id INT,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    salary NUMERIC(10, 2),
    department_id INT,
    MONTH VARCHAR(20),
    PRIMARY KEY (employee_id, month)
);
-- Insert data into the employees table with consistent employee_id and monthly salary variations
INSERT INTO employees_history (employee_id, first_name, last_name, salary, department_id, month) VALUES
-- Department 1: John Doe
(1, 'John', 'Doe', 60000, 1, 'January'),
(1, 'John', 'Doe', 61000, 1, 'February'),
(1, 'John', 'Doe', 60500, 1, 'March'),
-- Department 1: Jane Smith
(2, 'Jane', 'Smith', 80000, 1, 'January'),
(2, 'Jane', 'Smith', 82000, 1, 'February'),
(2, 'Jane', 'Smith', 81500, 1, 'March'),
-- Department 1: Jerry Gray
(3, 'Jerry', 'Gray', 82000, 1, 'January'),
(3, 'Jerry', 'Gray', 83000, 1, 'February'),
(3, 'Jerry', 'Gray', 82500, 1, 'March'),
-- Department 2: Jim Brown
(4, 'Jim', 'Brown', 90000, 2, 'January'),
(4, 'Jim', 'Brown', 91000, 2, 'February'),
(4, 'Jim', 'Brown', 90500, 2, 'March'),
-- Department 2: Jack Black
(5, 'Jack', 'Black', 95000, 2, 'January'),
(5, 'Jack', 'Black', 96000, 2, 'February'),
(5, 'Jack', 'Black', 95500, 2, 'March'),
-- Department 3: Jake White
(6, 'Jake', 'White', 70000, 3, 'January'),
(6, 'Jake', 'White', 71000, 3, 'February'),
(6, 'Jake', 'White', 70500, 3, 'March'),
-- Department 3: Jill Green
(7, 'Jill', 'Green', 75000, 3, 'January'),
(7, 'Jill', 'Green', 76000, 3, 'February'),
(7, 'Jill', 'Green', 75500, 3, 'March');


SELECT employee_id, first_name, last_name, e.department_id, e.month, 
	MAX(salary) OVER (PARTITION BY employee_id) AS max_salary,
	MIN(salary) OVER (PARTITION BY employee_id) AS min_salary,
	AVG(salary) OVER (PARTITION BY employee_id) AS avg_salary,
	SUM(salary) OVER (PARTITION BY employee_id) AS sum_salary,
	COUNT(employee_id) OVER (PARTITION BY e.department_id) AS employee_count
FROM employees_history AS e



SELECT employee_id, first_name, last_name, salary, e.month,
       LEAD(salary, 1) OVER (PARTITION BY employee_id) AS next_salary,
	   LAG(salary, 1) OVER (PARTITION BY employee_id) AS next_salary
FROM employees_history AS e;


SELECT employee_id, first_name, last_name, salary,
       FIRST_VALUE(salary) OVER (ORDER BY salary) AS first_salary
FROM employees_history AS e;


SELECT employee_id, first_name, last_name, salary, e.month,
       SUM(salary) OVER (PARTITION BY employee_id ORDER BY salary ROWS BETWEEN 1 PRECEDING AND CURRENT ROW) AS sum_salary_between_previous_and_current,
	   SUM(salary) OVER (PARTITION BY employee_id ORDER BY salary ROWS BETWEEN 1 PRECEDING AND 1 FOLLOWING) AS sum_salary_between_previous_and_following
FROM employees_history AS e;


SELECT employee_id, first_name, last_name, salary, e.month,
       AVG(salary) OVER (PARTITION BY department_id ORDER BY e.month RANGE BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW) AS avg_salary_range,
	   AVG(salary) OVER (PARTITION BY department_id ORDER BY e.month ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW) AS avg_salary_rows
FROM employees_history AS e;


WITH EmployeeSalaries AS (
    SELECT employee_id, first_name, last_name, department_id, salary,
           RANK() OVER (PARTITION BY department_id ORDER BY salary DESC) AS salary_rank
    FROM employees_history AS e
)
SELECT * FROM EmployeeSalaries
WHERE salary_rank = 1;


SELECT employee_id, first_name, last_name, salary,
       (SELECT AVG(salary) FROM employees WHERE department_id = e.department_id) AS dept_avg_salary
FROM employees_history AS e
WHERE salary > (SELECT AVG(salary) FROM employees WHERE department_id = e.department_id);