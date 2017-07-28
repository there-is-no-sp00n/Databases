#ITEM 4

#Q1
SELECT *
FROM EMPLOYEE
WHERE l_name='Jones' OR l_name='James';

#Q2
SELECT *
FROM EMPLOYEE
WHERE f_name='Kim' OR f_name='Wilson';

#Q3
SELECT E.ssn, E.f_name, E.l_name, SUM(W.hours), COUNT(W.e_ssn)
FROM EMPLOYEE AS E, WORKS_ON AS W
WHERE E.ssn=W.e_ssn
GROUP BY E.ssn, E.f_name, E.l_name
HAVING COUNT(W.e_ssn)> 1;


#Q4
SELECT D.d_name, D.d_number, L.d_location, SUM(salary)
FROM DEPARTMENT AS D, DEPT_LOCATIONS AS L, EMPLOYEE AS E
WHERE E.d_no=D.d_number AND D.d_number=L.d_number
GROUP BY D.d_name, D.d_number, L.d_location;

#SELECT d_no, salary
#From EMPLOYEE
#where d_no=4

#SELECT p_number, p_name, COUNT(*)
#FROM	PROJECT, WORKS_ON
#WHERE	p_number=p_no
#GROUP BY p_number, p_name
#HAVING	COUNT(*) > 2 ;

#Q5
SELECT P.p_name, P.p_number, P.p_location, COUNT(*)
FROM PROJECT AS P, WORKS_ON as W
WHERE W.p_no=P.p_number
GROUP BY P.p_name, P.p_number, P.p_location;

#Q6
SELECT DISTINCT E.ssn, E.f_name, E.l_name, P.p_number, P.p_name, W.hours, P.d_num, P.p_location
FROM EMPLOYEE AS E, PROJECT AS P, WORKS_ON AS W
WHERE P.d_num=5 AND P.p_location='Houston' AND W.e_ssn=E.ssn;

#Q7
SELECT E.l_name, E.f_name,SUM(W.hours) as tot_hours
FROM EMPLOYEE as E, WORKS_ON as W, PROJECT AS P
WHERE P.p_number=W.p_no AND W.e_ssn=E.ssn
GROUP BY E.l_name, E.f_name
HAVING tot_hours > 40;

#Q8
SELECT S.l_name, S.f_name, COUNT(*) as tot_emp
FROM EMPLOYEE AS E, EMPLOYEE AS S
WHERE E.super_ssn=S.ssn
GROUP BY S.l_name, S.f_name
ORDER BY S.l_name;

#Q9
SELECT P.p_name, SUM(W.hours) as tot_on_proj
FROM PROJECT AS P, WORKS_ON AS W, EMPLOYEE AS E
WHERE E.ssn=W.e_ssn AND P.p_number=W.p_no
GROUP BY P.p_name;
