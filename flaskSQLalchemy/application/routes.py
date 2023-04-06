from flask import render_template, jsonify, request
from application.models.manager import Manager

from application import app, service


@app.route('/employees', methods=['GET'])
def show_employees():
    error = ""
    employees = service.get_all_employees()
    if len(employees) == 0:
        error = "There are no employees to display"
    return render_template('employees.html', employees=employees, message=error)
    #return jsonify(employees)


# this is a ReST endpoint - only returns data
@app.route('/employees/<int:emp_id>', methods=['GET'])
def show_employee(emp_id):
    error = ""
    employee = service.get_employee_by_id(emp_id)
    if not employee:
        return jsonify("There is no employee with ID: " + str(emp_id))
    else:
        print(employee.first_name, employee.last_name)
    return jsonify(employee)


@app.route('/managers/<int:man_id>', methods=['GET'])
def get_manager(man_id):
    error = ""
    manager = service.get_manager_by_id(man_id)
    if not manager:
        error = "There is no manager with ID: " + str(man_id)
    return render_template('manager.html', manager=manager, message=error, title="Manager and Employees")
    #return jsonify(manager)

@app.route('/managers', methods=['POST'])
def create_manager():
    # data is a dictionary
    data = request.get_json()
    # need to create an object of type Manager with the data
    man = Manager(first_name = data['first_name'],last_name = data['last_name'] )
    print(man)
    service.save_new_manager(man)
    return jsonify(man)

