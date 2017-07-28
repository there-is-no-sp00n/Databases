#ITEM 5

#this query violates entity integrity, primary key 3 already exists
INSERT INTO DEPARTMENT
values('Public Relations', 3, '990110110', '2016-5-12');

#this query violates referential integrity, department number 100 does not exist in DEPTARTMENT table
INSERT INTO PROJECT
values('FIFA 18', 100, 'Arlington', 100);

#this query violates unique key constraints, the department name HR already exists
INSERT INTO DEPARTMENT
values('HR', 15, 294374738, '2017-7-15');


#ITEM 6

#this query violates referential integrity
DELETE FROM DEPARTMENT
WHERE d_number=1;


#ITEM 7

#these are the successful queries
INSERT INTO DEPARTMENT
values('Game Development', 15, 111111102, '2017-6-30');

INSERT INTO PROJECT
values('FIFA 18', 100, 'Arlington', 15);

INSERT INTO DEPARTMENT
values('PR', 20, 242916639, '2015-12-12');
