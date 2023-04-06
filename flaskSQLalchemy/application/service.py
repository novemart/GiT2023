from application.models.employee import Employee
from application.models.manager import Manager
from application import db

def get_all_employees():
    return db.session.query(Employee).all()


def get_employee_by_id(emp_id):
    if emp_id > 0:
        return db.session.query(Employee).filter_by(emp_id=emp_id).first()
    else:
        return None


def get_manager_by_id(man_id):
    if man_id < 100:
        manager = db.session.query(Manager).filter_by(man_id=man_id).first()
        return manager
    else:
        return None

def save_new_manager(man):
    db.session.add(man)
    db.session.commit()