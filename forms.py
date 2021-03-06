from psycopg2.extras import NamedTupleCursor
from wtforms import validators
from flask_wtf import FlaskForm as Form
from flask_wtf.file import FileField, FileAllowed, FileRequired
from wtforms import StringField, PasswordField, HiddenField, \
    IntegerField, SelectField
from wtforms.validators import DataRequired
from wtforms.fields.html5 import DateField, EmailField


class LoginForm(Form):
    login = StringField('login', validators=[DataRequired()],
                        render_kw={"placeholder": "login"})
    password = PasswordField('password', validators=[DataRequired()],
                             render_kw={"placeholder": "password"})


class RegistrationForm(Form):
    login = StringField('login', validators=[DataRequired()],
                        render_kw={"placeholder": "login"})
    password = PasswordField('password', validators=[DataRequired()],
                             render_kw={"placeholder": "password"})
    email = EmailField('email', validators=[DataRequired()],
                       render_kw={"placeholder": "email"})


class NewChainForm(Form):
    chain_name = StringField('chain_name', validators=[DataRequired()],
                             render_kw={"placeholder": "chain name",
                                        "class": "form-control"})


class AdminForm(Form):
    login = StringField('login', validators=[DataRequired()],
                        render_kw={"placeholder": "Login", "class": "form-control"})
    password = PasswordField('password', validators=[DataRequired()],
                             render_kw={"placeholder": "Password", "class": "form-control"})
    email = EmailField('email', validators=[DataRequired()],
                       render_kw={"placeholder": "Email", "class": "form-control"})
    chain_name = HiddenField('chain_name', validators=[DataRequired()])
    location = StringField('location', validators=[DataRequired()],
                           render_kw={"placeholder": "Hotel",
                                      "class": "form-control"})
    first_name = StringField('first_name', validators=[DataRequired()],
                             render_kw={"placeholder": "First name", "class": "form-control"})
    last_name = StringField('last_name', validators=[DataRequired()],
                            render_kw={"placeholder": "Last name", "class": "form-control"})
    salary = IntegerField('salary', validators=[DataRequired()],
                          render_kw={"placeholder": "Salary", "class": "form-control"})


class SearchForm(Form):
    from_date = DateField('from_date', validators=[DataRequired()], format='%d/%m/%Y',
                          render_kw={"class": "form-control"})
    to_date = DateField('to_date', validators=[DataRequired()], format='%d/%m/%Y',
                        render_kw={"class": "form-control"})
    max_price = IntegerField('price', validators=[DataRequired()],
                             render_kw={"placeholder": "Maximum price", "class": "form-control"})
    city = StringField('city', validators=[DataRequired()],
                       render_kw={"placeholder": "City", "class": "form-control"})
    capacity = IntegerField('capacity', validators=[DataRequired()],
                            render_kw={"placeholder": "Number of guests", "class": "form-control"})


class LocationForm(Form):
    location = StringField('location', validators=[DataRequired()],
                           render_kw={"placeholder": "Name of new hotel", "class": "form-control"})
    city = StringField('city', validators=[DataRequired()],
                       render_kw={"placeholder": "City", "class": "form-control"})
    chain_name = HiddenField('chain_name', validators=[DataRequired()])
    address = StringField('address', validators=[DataRequired()],
                          render_kw={"placeholder": "Address", "class": "form-control"})

class DeleteLocationForm(Form):
    location = StringField('location', validators=[DataRequired()],
                           render_kw={"placeholder": "name of new hotel", "class": "form-control"})
    chain_name = HiddenField('chain_name', validators=[DataRequired()])

class DeleteChainForm(Form):
    chain_name = HiddenField('chain_name', validators=[DataRequired()])


class ReservationForm(Form):
    first_name = StringField('first_name', validators=[DataRequired()],
                             render_kw={"placeholder": "First name", "class": "form-control"})
    last_name = StringField('last_name', validators=[DataRequired()],
                             render_kw={"placeholder": "Last name", "class": "form-control"})
    ssn = StringField('ssn', validators=[DataRequired()],
                             render_kw={"placeholder": "Social Security Number", "class": "form-control"})
    email = EmailField('email', validators=[DataRequired()],
                       render_kw={"placeholder": "E-mail", "class": "form-control"})
    country_code = StringField('country_code', validators=[DataRequired(), validators.length(max=3)],
                          render_kw={"placeholder": "Country code", "class": "form-control"})
    roomtype_id = HiddenField('roomtype_id', validators=[DataRequired()])
    check_in = HiddenField('check_in', validators=[DataRequired()])
    check_out = HiddenField('check_out', validators=[DataRequired()])


class RoomTypeForm(Form):
    chain_name = HiddenField('chain_name', validators=[DataRequired()])
    location = HiddenField('location', validators=[DataRequired()])
    name = StringField('name', validators=[DataRequired()],
                       render_kw={"placeholder": "name", "class": "form-control"})
    price = IntegerField('price', validators=[DataRequired()],
                         render_kw={"placeholder": "price", "class": "form-control"})
    capacity = IntegerField('capacity', validators=[DataRequired()],
                            render_kw={"placeholder": "capacity", "class": "form-control"})


class RoomForm(Form):
    room_type = SelectField('id', validators=[DataRequired()],
                            render_kw={"class": "form-control"})
    roomNo = IntegerField('roomNo', validators=[DataRequired()],
                          render_kw={"placeholder": "number", "class": "form-control"})


class CheckinForm(Form):
    ssn = StringField('ssn', validators=[DataRequired()],
                             render_kw={"placeholder": "Social Security Number", "class": "form-control"})
    country = StringField('country', validators=[DataRequired(), validators.length(max=3)],
                          render_kw={"placeholder": "Country code", "class": "form-control"})


class UploadForm(Form):
    image = FileField('image', validators=[
        FileRequired(),
        FileAllowed(['jpg'], 'Images only!')
    ])
    chain_name = HiddenField('chain_name', validators=[DataRequired()])
    location = HiddenField('location', validators=[DataRequired()])
