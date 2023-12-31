from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField
from wtforms.validators import Length,Email, EqualTo,Email,DataRequired,ValidationError
from market.models import User

class RegisterForm(FlaskForm):
    def validate_username(self, username_to_check):
        username_to_check = username_to_check.data.lower()
        user = User.query.filter_by(username=username_to_check).first()
        if user:
            raise ValidationError("Username already exist")
    def validate_email_address(self, email_to_check):
        email_to_check =email_to_check.data.lower()
        email_address = User.query.filter_by(email_address=email_to_check).first()
        if email_address:
            raise ValidationError("Email address already exist")

    username = StringField(label="User Name:", validators=[Length(min=2,max=30),DataRequired()])
    email_address = StringField(label="Email Address:",validators=[Email(),DataRequired()])
    password1 = PasswordField(label="Password:", validators=[Length(min=6),DataRequired()])
    password2 = PasswordField(label="Confirm Password:",validators=[EqualTo('password1'),DataRequired()])
    submit = SubmitField(label="Create Account")


class LoginForm(FlaskForm):
    username = StringField(label="User name", validators= [DataRequired()])
    password= PasswordField(label="Password",validators=[DataRequired()])
    submit = SubmitField(label="Sign in")
