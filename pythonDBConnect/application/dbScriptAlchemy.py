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

manager = session.query(Manager).filter_by(first_name="Santa").first()
print(manager.first_name, manager.last_name, manager.man_id, manager.employees)
for e in manager.employees:
    print(e.first_name, end = " ")
    print(e.last_name)

#
#
# manager object
manager = Manager(first_name="Man1", last_name="Man2")
# inserting it into the database
session.add(manager)
# don't forget to commit!
session.commit()
