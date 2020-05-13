from flask import render_template, flash, redirect, url_for
from flask_login import login_user, current_user, logout_user
from datetime import datetime
from app import app
from app.forms import LoginForm
from app.models import User

@app.route('/')
def index():
	user = {'username':'sagar'}
	posts= [
		{
			'author': {'username':'Sagar'},
			'body': 'Beautiful day in Kathmandu!'
		},
		{
			'author': {'username': 'Sagar'},
			'body': 'This is a good day'
		}
	]
	return render_template('index.html', user = user, posts=posts)


@app.route('/login', methods=['GET', 'POST'])
def login():
	# if already login, redirect to index page
	if current_user.is_authenticated:
		return redirect(url_for('index'))
	form = LoginForm()
	# if request comes from form on submit after validation
	if form.validate_on_submit():
		#flash("Form Information Received for user {}, remember_me = {}".format(form.username.data, form.remember_me.data))
		user = User.query.filter_by(username = form.username.data).first()
		if (user is None or not user.check_password(form.password.data)):
			flash("Invalid username or passowrd")
			# take username from form and search the database
			return redirect(url_for('login'))
		login_user(user, remember=form.remember_me.data, )
		return redirect(url_for('index'))
	return render_template('login.html', title="Sign In", form=form)

@app.route('/logout')
def logout():
	logout_user()
	return redirect(url_for('index'))