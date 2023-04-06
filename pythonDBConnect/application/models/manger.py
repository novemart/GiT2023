from sqlalchemy.orm import backref

from application import db
from dataclasses import dataclass

# the annotation below will help to turn the Python object into a JSON object
class Manager(db.Model):

    man_id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)

    employees = db.relationship('Employee', back_populates="manager", cascade="all, delete", passive_deletes=True)