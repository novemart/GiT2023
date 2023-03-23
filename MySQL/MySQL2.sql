use Company;
select * from employee;
select * from manager;

-- watch out, no warning, can't go back
drop table manager;

-- create
-- insert only some of the values
insert into manager(first_name, last_name) values ("Santa", "Claus");

-- insert multiple rows at the same time
insert into manager(first_name, last_name) values ("Christmas", "Elf"), ("Robin","Hood"), ("Jane", "Eyre");

insert into manager(first_name, last_name) values ("Jack", "Sparrow");

insert into manager values (4, "Mickey", "Mouse");
insert into employee values ( 2, "Tom", "Cat", 7, "IT", "OPS", 2);
insert into employee values ( 3, "Jerry", "Mouse", 6, "LAW", "A", 3);
insert into employee (first_name, last_name, dep_id, dep_name, emp_role) values ( "Cinda", "Rella", 6, "LAW", "A");


-- update
-- if no where clause then update performed on all rows
-- update and delete would require the where clause to use the primary key field
update manager set last_name="Rochester" where man_id=5;

update manager set first_name=null where man_id=3;

update employee set manager_id = 2 where emp_id = 1;

-- delete 
delete from manager where man_id = 4;

delete from manager where man_id = 1;

-- read
select * from employee;

-- only select some of the columns
select first_name, last_name, manager_id from employee;

-- only select some of the columns for a specific row
select first_name, last_name from employee where manager_id = 2;

-- alias for returned columns
-- != not equal
select first_name as fname, last_name as lname from employee where manager_id != 2;

-- sort the result based on values from a specific column
select * from employee order by first_name;

-- default ascending, desc = descending order
select * from employee order by emp_role desc;

-- if multiple name alias it needs to be in ""
-- virtual calculated column, no change performed on the stored data
select first_name fname, last_name lname, dep_id * 3.5 as "employee age" from employee;

-- concatenate multiple columns and give it alias
select concat(first_name,' ', last_name) as 'full name' from employee;

-- unique values
select distinct manager_id from employee;

-- count unique values
select count(distinct manager_id) from employee;

-- where clause using comparison rather than equality
select * from employee where dep_id > 6;

-- logical or
select first_name, last_name, manager_id from employee where first_name = "Tooth" or first_name = "tom";

-- match one of the values in the set
select first_name, last_name, manager_id from employee where first_name in ("Tooth", "Tom", "Martina");

-- select everyone whose name starts with T
select * from employee where first_name like "T%";

-- SQL language is case insensitive
Select * FROm employee where first_name like "t%";

-- joins
select * from employee;

-- default inner join - only the matched rows will be printed
select * from employee join manager on manager_id = man_id;

-- all rows from manager table, if a manager manages an employee, their information will be printed as well
select * from employee right outer join manager on manager_id = man_id;

-- all rows from employee table, if an employee has a manager, their information will be printed as well
select * from employee left outer join manager on manager_id = man_id;

-- select only certain columns from those two tables
select e.first_name, e.last_name, m.first_name, m.last_name from employee e inner join manager m on manager_id = man_id;























