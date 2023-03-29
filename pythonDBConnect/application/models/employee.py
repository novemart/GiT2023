from application import db

# ORM - Object relational mapping - mapping class to a table
# DTO - data transfer object
class Employee(db.Model):
    emp_id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50), nullable=True)
    last_name = db.Column(db.String(50), nullable=False)
    dep_id= db.Column(db.Integer, nullable = False)
    dep_name = db.Column(db.String(5), nullable=True)
    emp_role=db.Column(db.String(20), nullable=True)
    manager_id=db.Column(db.Integer, db.ForeignKey('manager.man_id'), nullable = True)
