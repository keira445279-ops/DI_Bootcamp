-- *******************************
-- create table book and insert
-- *******************************

-- Create table book (
-- book_id SERIAL PRIMARY KEY, 
-- title varchar(100) NOT NULL, 
-- author varchar(100) NOT NULL
-- );

-- Insert into book (title, author)
-- values
-- 	('Alice In Wonderland', 'Lewis Carroll'),
-- 	('Harry Potter', 'J.K Rowling'),
-- 	('To kill a mockingbird', 'Harper Lee');

-- select *
-- from book


-- *********************************
-- create table student and insert
-- *********************************

-- Create table student(
-- student_id SERIAL PRIMARY KEY, 
-- name varchar(100) NOT NULL UNIQUE, 
-- age smallint check (age <= 15) 
-- );

-- Insert into student(name, age)
-- values
-- 	('John', 12),
-- 	('Lera', 11),
-- 	('Patrick', 10),
-- 	('Bob', 14);

-- select *
-- from student


-- *********************************
-- create table library and insert
-- *********************************

-- Create table library(
-- book_fk_id int references book(book_id) ON DELETE CASCADE ON UPDATE CASCADE,
-- student_id int references student(student_id) ON DELETE CASCADE ON UPDATE CASCADE,
-- borrowed_date date not null,
-- primary key (book_fk_id, student_id)
-- )

-- insert into library (book_fk_id, student_id, borrowed_date)
-- values
-- 	((select book_id from book where title = 'Alice In Wonderland'), 
-- 	(select student_id from student where name = 'John'), '15/02/2022'),
-- 	((select book_id from book where title = 'To kill a mockingbird'), 
-- 	(select student_id from student where name = 'Bob'), '03/03/2021'),
-- 	((select book_id from book where title = 'Alice In Wonderland'), 
-- 	(select student_id from student where name = 'Lera'), '23/05/2021'),
-- 	((select book_id from book where title = 'Harry Potter'), 
-- 	(select student_id from student where name = 'Bob'), '12/08/2021')


-- **Select all the columns from the junction table**

-- select *
-- from library


-- **Select the name of the student and the title of the borrowed books**

-- select s.name, b.title
-- from library as l
-- inner join student as s on s.student_id = l.student_id
-- inner join book as b on b.book_id = l.book_fk_id
-- order by s.name


-- **Select the average age of the children, that borrowed the book Alice in Wonderland**

-- select round(avg(s.age), 2)
-- from library as l
-- inner join student as s on s.student_id = l.student_id
-- inner join book as b on b.book_id = l.book_fk_id


-- **Delete a student from the Student table, what happened in the junction table ?**

-- delete from student where name = 'John'

-- select *
-- from library

-- this student was deleted from library table because we`ve used cascade
