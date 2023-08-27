from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import Length, Email, EqualTo, DataRequired


class RegisterForm(FlaskForm):

    username = StringField(label="Username: ", validators=[Length(min=2), DataRequired()])
    email = StringField(label="Email: ", validators=[Email(), DataRequired()])
    password1 = PasswordField(label="Password: ", validators=[Length(min=7), DataRequired()])
    password2 = PasswordField(label="Confirm Password: ", validators=[EqualTo('password1'), DataRequired()])
