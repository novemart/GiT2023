-- create an empty database = schema, safe bubble for our table; usually one per application
create database Company;

-- telling the server which database we will be working with; there may be multiple databases on the server
use Company;

-- create a table to store information about managers
-- we need to specify all the columns with their data type
-- and constraints; i.e. not null (can not ber left blank); auto_increment (the server can do some counting for us)
-- it's also possible to set a default value or set a check on a column
create table if not exists manager(
	man_id smallint not null primary key auto_increment,
    first_name varchar(50),
    last_name varchar(50) not null );

-- once we have an empty table we can start putting some data insert
-- make sure the values go in the right order, otherwise it will be rejected!    
insert into manager values (1, "Martina", "Yusuf");

-- sanity check; get all values from the table
select * from manager;

-- creating the table for employee
-- notice the way we specify the foreign key column - we need to say with table it refers to and what column in that table
create table employee(
	emp_id smallint not null primary key auto_increment,
    first_name varchar(50),
    last_name varchar(50) not null,
    dep_id smallint not null,
    dep_name varchar(5),
    emp_role varchar(20),
    manager_id smallint,
    foreign key(manager_id) references manager(man_id) );

-- inserting data into the employee table
insert into employee values ( 1, "Tooth", "Fairy", 7, "IT", "HR", 1);

-- referential integrity - manager with id 3 does not exist! this is being checked while the data is being inserted
-- this line will therefore give us an error    
insert into employee values ( 1, "Tooth", "Fairy", 7, "IT", "HR", 3); 


-- checking that the data is saved in the employee table
select * from employee;