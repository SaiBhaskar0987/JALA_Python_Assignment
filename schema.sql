CREATE DATABASE jala_academy;
USE jala_academy;

CREATE TABLE employees (
    id INT PRIMARY KEY,
    name VARCHAR(100),
    department VARCHAR(50),
    salary INT,
    joining_date DATE,
    city VARCHAR(50)
);

INSERT INTO employees VALUES
(1, 'Alice', 'HR', 50000, '2021-01-15', 'Hyderabad'),
(2, 'Bob', 'Finance', 60000, '2020-03-22', 'Bangalore'),
(3, 'Charlie', 'IT', 75000, '2019-07-10', 'Chennai'),
(4, 'David', 'HR', 52000, '2022-02-01', 'Hyderabad'),
(5, 'Eva', 'IT', 80000, '2018-11-25', 'Mumbai'),
(6, 'Frank', 'Finance', 55000, '2020-08-17', 'Bangalore'),
(7, 'Grace', 'Marketing', 62000, '2021-04-11', 'Pune'),
(8, 'Helen', 'IT', 90000, '2023-01-01', 'Chennai'),
(9, 'Ian', 'HR', 48000, '2021-06-30', 'Hyderabad'),
(10, 'Jack', 'Marketing', 61000, '2022-09-15', 'Pune'),
(11, 'Kathy', 'Finance', 57000, '2020-10-20', 'Mumbai'),
(12, 'Leo', 'IT', 87000, '2019-12-12', 'Chennai'),
(13, 'Mona', 'Marketing', 64000, '2023-02-02', 'Bangalore'),
(14, 'Nina', 'HR', 51000, '2021-08-19', 'Hyderabad'),
(15, 'Oscar', 'Finance', 63000, '2022-05-01', 'Mumbai');

SELECT * FROM employees;

INSERT INTO employees VALUES (16, 'Peter', 'IT', 82000, '2023-03-03', 'Delhi');

SELECT * FROM employees WHERE department = 'IT';

UPDATE employees SET salary = 66000 WHERE id = 2;

DELETE FROM employees WHERE id = 16;

SELECT COUNT(*) FROM employees;

SELECT COUNT(*) FROM employees WHERE department = 'HR';

SELECT department, MAX(salary) FROM employees GROUP BY department;

SELECT department, MIN(salary) FROM employees GROUP BY department;

SELECT name FROM employees WHERE joining_date > '2022-01-01';

SELECT * FROM employees ORDER BY salary DESC;

SELECT name FROM employees WHERE salary BETWEEN 50000 AND 70000;

SELECT * FROM employees WHERE name LIKE 'A%';

SELECT DISTINCT city FROM employees;

SELECT department, COUNT(*) FROM employees GROUP BY department HAVING COUNT(*) > 2;
