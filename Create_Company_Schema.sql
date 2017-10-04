CREATE DATABASE `COMPANY`;

USE `COMPANY`;

CREATE TABLE `COMPANY`.`EMPLOYEE` 
(
  `f_name` VARCHAR(30) NOT NULL,
  `m_init` CHAR,
  `l_name` VARCHAR(30) NOT NULL,
  `ssn` INT NOT NULL,
  `b_date` DATE,
  `address` VARCHAR(30) NULL,
  `sex` CHAR,
  `salary` INT,
  `super_ssn` INT,
  `d_no` INT NOT NULL,
  PRIMARY KEY(ssn),
  FOREIGN KEY(super_ssn) REFERENCES EMPLOYEE(ssn)
);

CREATE TABLE `COMPANY`.`DEPARTMENT`
(
	`d_name` varchar(30) NOT NULL,
    `d_number` INT NOT NULL,
	`mgr_ssn` INT NOT NULL,
    `mgr_start_date` DATE,
    PRIMARY KEY (d_number),
    UNIQUE (d_name),
    FOREIGN KEY (mgr_ssn) REFERENCES EMPLOYEE(ssn)
);

CREATE TABLE `COMPANY`.`DEPT_LOCATIONS`
(
	d_number INT NOT NULL,
    d_location VARCHAR(15) NOT NULL,
    PRIMARY KEY	(d_number, d_location),
    FOREIGN KEY (d_number) REFERENCES DEPARTMENT(d_number)
);

CREATE TABLE `COMPANY`.`PROJECT`
(
	`p_name` VARCHAR(30) NOT NULL,
    `p_number` INT NOT NULL,
    `p_location` VARCHAR(30) NOT NULL,
    `d_num` INT NOT NULL,
    PRIMARY KEY (p_number),
    FOREIGN KEY(d_num) REFERENCES DEPARTMENT(d_number)
);

CREATE TABLE `COMPANY`.`WORKS_ON`
(
	`e_ssn` INT NOT NULL,
    `p_no` INT NOT NULL,
    `hours` FLOAT NOT NULL,
    PRIMARY KEY (e_ssn, p_no),
    FOREIGN KEY(e_ssn) REFERENCES EMPLOYEE(ssn),
    FOREIGN KEY(p_no) REFERENCES PROJECT(p_number)
);

ALTER TABLE EMPLOYEE
ADD FOREIGN KEY(d_no) REFERENCES DEPARTMENT(d_number)
