from sqlalchemy import create_engine
from sqlalchemy import text

# using root user is not a great idea!!
user = 'root'
password = ''
host = '127.0.0.1'
port = 3306
database = 'Company'

# PYTHON FUNCTION TO CONNECT TO THE MYSQL DATABASE AND
# RETURN THE SQLACHEMY ENGINE OBJECT
def get_connection():
    # mysql+pymysql://root:@127.0.0.1:3306/Company
    return create_engine(
        url="mysql+pymysql://{0}:{1}@{2}:{3}/{4}".format(
            user, password, host, port, database))

engine = get_connection()

# try:
#     with engine.connect() as conn:
#         result = conn.execute(text("SELECT * FROM manager"))
#         for row in result:
#          print(f"First Name: {row.first_name}  Last Name: {row.last_name}")
# except Exception as e:
#     print("Exception Happened")
#     print(e)

print('******parameterised query ********')

# num = int(input("What manager would you like? "))
# with engine.connect() as conn:
#     result = conn.execute(
#         text("SELECT first_name, last_name FROM manager WHERE man_id = :param"),
#         {"param": num}
#     )
#     for row in result:
#         print(f"First Name: {row.first_name}  Last Name: {row.last_name}")

# name = input("What manager would you like? ")
# with engine.connect() as conn:
#     result = conn.execute(
#         text("SELECT first_name, last_name FROM manager WHERE first_name = :param"),
#         {"param": name}
#     )
#     for row in result:
#         print(f"First Name: {row.first_name}  Last Name: {row.last_name}")


# print('************* join *********')
# fname = input("What first name employee would you like? ")
# lname = input("What last name employee would you like? ")
#
# with engine.connect() as conn:
#     result = conn.execute(
#         text("""select e.first_name emp_fname, e.last_name emp_lname, e.dep_id, e.dep_name, e.emp_role, m.first_name , m.last_name
#         from employee e inner join manager m
#         on e.manager_id= m.man_id where e.first_name = :fname and e.last_name= :lname"""),
#         {"fname": fname, "lname" : lname}
#     )
#     for row in result:
#         print(f"First Name: {row.emp_fname}  Last Name: {row.emp_lname} Dep Id: {row.dep_id} Role: {row.emp_role} Manager: {row.first_name + row.last_name}")


with engine.connect() as conn:
    result = conn.execute(
        text("""update manager set first_name = 'Christmas' where man_id = 3""")
    )
    conn.commit()