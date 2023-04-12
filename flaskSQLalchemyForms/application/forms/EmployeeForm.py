from flask_wtf import FlaskForm

from wtforms import StringField, SubmitField, IntegerField, SelectField
from wtforms.ext.sqlalchemy.fields import QuerySelectField

from application.models.manager import Manager


class EmployeeForm(FlaskForm):
    first_name = StringField('Employee First Name')
    last_name = StringField('Employee Last Alias')
    dep_name = StringField('Department Name')
    dep_id = IntegerField('Department ID')

    manager_list = QuerySelectField(
        'Manager',
        query_factory=lambda: Manager.query,
        allow_blank=False,
        get_label = 'last_name'
    )
    submit = SubmitField('Add Employee')