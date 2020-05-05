import os

class Config(object):
	#app.config['SECRET_KEY'] = "I-am-Unguessable"
	SECRET_KEY = os.environ.get('SECRET_KEY') or "I-am-Unguessable"