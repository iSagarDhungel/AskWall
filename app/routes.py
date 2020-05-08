from flask import render_template, flash, redirect, url_for
from datetime import datetime
from app import app
from app.forms import LoginForm

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
	form = LoginForm()
	# if request comes from form on submit after validation
	if form.validate_on_submit():
		flash("Form Information Received for user {}, remember_me = {}".
			format(form.username.data, form.remember_me.data))

		return redirect({{ url_for('index') }})
	return render_template('login.html', title="Sign In", form=form)
