from flask import *
from datetime import datetime
from app import app


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


@app.route('/login')
def login():
	form = LoginForm()
	return render_template('login.html', title="Sign In", form=form)
