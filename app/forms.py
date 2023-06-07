from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField



class LoginForm(FlaskForm):
    employee_number = StringField('employee_number')
    password = PasswordField('Password')
    submit = SubmitField('xxSubmitxx')
