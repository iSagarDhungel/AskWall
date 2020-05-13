from flask import render_template, flash, redirect, url_for, request
from werkzeug.urls import url_parse
from flask_login import login_user, current_user, logout_user, login_required
from datetime import datetime
from app import app, db
from app.forms import LoginForm, RegistrationForm
from app.models import User

@app.route('/')
@app.route('/index')
@login_required
def index():
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
	return render_template('index.html', title = 'Home', posts=posts)


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
		login_user(user, remember=form.remember_me.data)

		next_page = request.args.get('next')
		if not next_page or url_parse(next_page).netloc != '':
			next_page = url_for('index')

		return redirect(next_page)
	return render_template('login.html', title="Sign In", form=form)

@app.route('/logout')
def logout():
	logout_user()
	return redirect(url_for('index'))

@app.route('/register', methods=['GET', 'POST'])
def register():
	if current_user.is_authenticated:
		return redirect(url_for('index'))

	form = RegistrationForm()
	if form.validate_on_submit():
		user = User(username= form.username.data, email = form.email.data)
		user.set_password(form.password.data)
		db.session.add(user)
		db.session.commit()
		flash('Congras, you are now a registered user')
		return redirect(url_for('login'))
	return render_template('register.html', title='Register', form=form)