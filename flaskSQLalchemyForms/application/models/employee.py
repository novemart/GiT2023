from application import db
from dataclasses import dataclass

# ORM - Object relational mapping - mapping class to a table
# DTO - data transfer object
@dataclass
class Employee(db.Model):
    # which attributes are included in the JSON that I'm sending back
    emp_id: int
    first_name: str
    last_name: str
    dep_id: str
    dep_name : str
    emp_role : str


    emp_id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50), nullable=True)
    last_name = db.Column(db.String(50), nullable=False)
    dep_id= db.Column(db.Integer, nullable = False)
    dep_name = db.Column(db.String(5), nullable=True)
    emp_role=db.Column(db.String(20), nullable=True)
    manager_id=db.Column(db.Integer, db.ForeignKey('manager.man_id', ondelete="CASCADE"), nullable = True)

    manager = db.relationship("Manager", back_populates="employees")