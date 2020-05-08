import os

rootdir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
	#app.config['SECRET_KEY'] = "I-am-Unguessable"
	SECRET_KEY = os.environ.get('SECRET_KEY') or "I-am-Unguessable"
	SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
		'sqlite:///' + os.path.join(rootdir, 'app.db')
	# track changes in object
	SQLALCHEMY_TRACK_MODIFICATION = False
