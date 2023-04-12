from flask import render_template, jsonify, request

from application.forms.EmployeeForm import EmployeeForm
from application.models.employee import Employee
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

@app.route('/new_employee', methods=['GET','POST'])
def add_new_employee():
    error = ""
    form = EmployeeForm()

    if request.method == 'POST':
        form = EmployeeForm(request.form)
        first_name = form.first_name.data
        last_name = form.last_name.data
        dep_name = form.dep_name.data
        dep_id = form.dep_id.data
        man = form.manager_list.data
        if len(first_name) == 0 or len(last_name) == 0:
            error = "Please supply both name and alias"
        else:
            emp = Employee(first_name=first_name, last_name=last_name,
                           dep_name = dep_name, dep_id = dep_id, manager=man)
            service.add_new_employee(emp)
            employees = service.get_all_employees()
            return render_template('employees.html', employees=employees, message=error)

    return render_template('new_employee_form.html', form=form, message=error)
