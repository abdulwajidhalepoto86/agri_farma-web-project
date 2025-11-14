from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, TextAreaField, SelectField, FileField, FloatField
from wtforms.validators import DataRequired, Email, Length, EqualTo, Optional
from flask_wtf.file import FileAllowed

# ------------------------------
# User Registration & Login
# ------------------------------
class RegisterForm(FlaskForm):
    name = StringField('Full Name', validators=[DataRequired(), Length(min=2)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=6)])
    confirm = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    profession = StringField('Profession', validators=[Optional()])
    expertise = SelectField('Expertise Level', choices=[('beginner','Beginner'),('intermediate','Intermediate'),('expert','Expert')])
    submit = SubmitField('Register')

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')

# ------------------------------
# Forum Posts & Comments
# ------------------------------
class PostForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    body = TextAreaField('Body', validators=[DataRequired(), Length(min=5)])
    category = SelectField('Category', coerce=int, validators=[Optional()])
    image = FileField('Image', validators=[Optional(), FileAllowed(['jpg','png','jpeg','gif'], 'Images only')])
    submit = SubmitField('Submit')

class CommentForm(FlaskForm):
    body = TextAreaField('Reply', validators=[DataRequired(), Length(min=1)])
    submit = SubmitField('Reply')

# ------------------------------
# Marketplace Product Form
# ------------------------------
class ProductForm(FlaskForm):
    name = StringField('Product Name', validators=[DataRequired()])
    description = TextAreaField('Description', validators=[Optional()])
    price = FloatField('Price', validators=[Optional()])
    image = FileField('Image', validators=[Optional(), FileAllowed(['jpg','png','jpeg','gif'], 'Images only')])
    submit = SubmitField('Add Product')

# ------------------------------
# Consultant Registration Form
# ------------------------------
class ConsultantForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    category = StringField('Expertise Category', validators=[Optional()])
    bio = TextAreaField('Bio', validators=[Optional()])
    contact = StringField('Contact', validators=[Optional()])
    submit = SubmitField('Register as Consultant')
