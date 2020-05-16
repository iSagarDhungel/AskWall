from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField
from app.models import User

from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError

class LoginForm(FlaskForm):
	"""docstring for LoginForm"""
	username = StringField('Username', validators=[DataRequired()])
	password = PasswordField('Password',  validators=[DataRequired()])
	remember_me = BooleanField('Remember Me')
	submit = SubmitField('Sign In')

class RegistrationForm(FlaskForm):
	"""docstring for LoginForm"""
	username = StringField('Username', validators=[DataRequired()])
	email = StringField('Email', validators=[DataRequired(), Email()])
	password = PasswordField('Password',  validators=[DataRequired()])
	password2 = PasswordField('Password',  validators=[DataRequired(), EqualTo('password')])
	submit = SubmitField('Register')

	''' Custom Validators 
	- use case: Search database for the username
	- should be on format def validate_entityname()
	'''
	def validate_username(self, username):
		user = User.query.filter_by(username=username.data).first()
		if user is not None:
			raise ValidationError('Please Use Different Username')

	def validate_email(self, email):
		user = User.query.filter_by(email=email.data).first()
		if user is not None:
			raise ValidationError('Please Use Different Email address')

class EditProfileForm(FlaskForm):
	username = StringField('Username', validators=[DataRequired()])
	about_me = TextAreaField('About me', validators=[Length(min=0, max=150)])
	submit = SubmitField('Submit')

