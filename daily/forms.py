from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import Length, Email, EqualTo, DataRequired, ValidationError
from daily.models import User

class RegisterForm(FlaskForm):

    def validate_username(self, username):
        userfield=User.query.filter_by(username=username.data).first()
        if userfield:
            raise ValidationError("Username already exists! Please try a different username")

    def validate_email(self, email):
        emailfield = User.query.filter_by(email=email.data).first()
        if emailfield:
            raise ValidationError("Email already exists! Please try a different email address")
    
    username = StringField(label="Username: ", validators=[Length(min=2), DataRequired()])
    email = StringField(label="Email: ", validators=[Email(), DataRequired()])
    password1 = PasswordField(label="Password: ", validators=[Length(min=7), DataRequired()])
    password2 = PasswordField(label="Confirm Password: ", validators=[EqualTo('password1'), DataRequired()])

class LoginForm(FlaskForm):
    email = StringField(label='Email: ', validators=[Email(), DataRequired()])
    password=PasswordField(label='Password: ', validators=[DataRequired()])
