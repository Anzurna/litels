from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, widgets, SelectMultipleField
from wtforms.validators import DataRequired, Length, Email, EqualTo

class RegistrationForm(FlaskForm):
    username = StringField("Username",
        validators=[DataRequired(), Length(min=2, max=90)])
    email = StringField("Email", 
        validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[DataRequired()])
    confirm_password = PasswordField("Confirm Password", 
        validators=[DataRequired(), EqualTo("password")])

    submit = SubmitField("Sign Up")

class LoginForm(FlaskForm):
    email = StringField("Email", 
        validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[DataRequired()])
    remember = BooleanField("Remember me")
    submit = SubmitField("Login")

class MultiCheckboxField(SelectMultipleField):
    widget = widgets.ListWidget(prefix_label=False)
    option_widget = widgets.CheckboxInput()

class SimpleForm(FlaskForm):
    # string_of_files = ['one\r\ntwo\r\nthree\r\n']
    # list_of_files = string_of_files[0].split()
    # # create a list of value/description tuples
    
    article_numbers = ["0", "1", "2", "3", "4"]
    numbers = [(x, x) for x in article_numbers]
    example = MultiCheckboxField('Label', choices=numbers)
    