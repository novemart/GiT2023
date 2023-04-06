from application import db
from application.models.manger import Manager
from application.models.employee import Employee
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
user = 'root'
password = ''
host = '127.0.0.1'
port = 3306
database = 'Company'

# PYTHON FUNCTION TO CONNECT TO THE MYSQL DATABASE AND
# RETURN THE SQLACHEMY ENGINE OBJECT
def get_connection():
    return create_engine(
        url="mysql+pymysql://{0}:{1}@{2}:{3}/{4}".format(
            user, password, host, port, database))

engine = get_connection()
Session = sessionmaker(bind=engine)

session = Session()

#select manager with manager_id
# returns one row -> turns it into an object
# manager = session.query(Manager).filter_by(man_id=3).first()
# print(manager.first_name, manager.last_name, manager.man_id, manager.employees)
# for e in manager.employees:
#     print(e.first_name, end = " ")
#     print(e.last_name)

#.all() will return all rows that match the filter -> in the form of a LIST of managers
# list_of_managers = session.query(Manager).filter_by(first_name="Martina").all()
# for man in list_of_managers:
#     print(man.first_name, man.last_name)

# list_of_managers = session.query(Manager).filter(Manager.man_id>3).all()
# for man in list_of_managers:
#     print("Manager: " ,man.first_name, man.last_name, end=' ')
#     print("Manages:")
#     for emp in man.employees:
#         print(emp.first_name, emp.last_name)


# manager object
# manager = Manager(first_name="Another", last_name="Manager")
# # adding employees to the manager list
# # e1 = Employee(first_name="Martin", last_name="Yusuf", dep_id = 6, dep_name="IT", emp_role="MAN")
# # e2 = Employee(first_name="Will", last_name="Trundle", dep_id = 5, dep_name="HR", emp_role="MAN")
# e1 = session.query(Employee).filter_by(emp_id=4).first()
# list_emp = [e1]
# manager.employees = list_emp
# # when saving manager -> saves their employees as well!!
# session.add(manager)
# # don't forget to commit!
# session.commit()

# delete still does not cascade!
manager = session.query(Manager).filter(Manager.man_id==4).first()
session.delete(manager)
session.commit()


# e1 = session.query(Employee).filter_by(emp_id=4).first()
# print(e1.first_name, e1.last_name, e1.manager.first_name, e1.manager.last_name)

# e1 = session.query(Employee).filter_by(emp_id=4).first()
# e1.first_name = "Snow"
# session.add(e1)
# session.commit()