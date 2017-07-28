USE COMPANY;

#ITEM 3

#Q1 - this fails because this entry has the same primary key as an existing one
#this violates the entity integrity
INSERT INTO DEPARTMENT
values('Services', 1, '123456789', '2012-08-11');

#Q2 - this fails because this entry has the same primary ket as an existing one
#this violates the entity integrity
INSERT INTO DEPARTMENT
values('Purchasing', 3, '990110110', '2013-2-2');

#Q3 - this query is successful because the primary key in this one has no duplicates
INSERT INTO DEPARTMENT
values ('Customers', 12, '333445555', '2013-1-14')

#Q4 - this query is successful because the department is not being changed to null
UPDATE DEPT_LOCATIONS
SET d_number = 9
WHERE d_location='Seattle';

#Q5 - this query does not affect any rows as an employee with ssn 444444444 does not exist
UPDATE EMPLOYEE
SET salary = 55000
WHERE ssn = 444444444;

#Q6 - this query fails as Ray King also has the same ssn as the new input data. Primary keys must be unique. Violates entity integrity
INSERT INTO EMPLOYEE
values('Jane', 'B', 'Smith', '666666606', '1980-3-1', '3556 W Second Street,Miami,FL', 'F', 85000, '666666603', 5);

#look into this Q7 - this query does not do anything as the employee with that SSN does not work on project 1 rather project 3
UPDATE WORKS_ON
SET hours=25
WHERE p_no=1 AND e_ssn=666884444;

#Q8 - this query fails as it violates referential integrity, other tables refers to this row
DELETE FROM EMPLOYEE
WHERE ssn=432765098;

#Q9 - this query fails as it violates referential integrity, other tables refers to this row
DELETE FROM DEPARTMENT
WHERE d_number=9;
