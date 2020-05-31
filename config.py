import os

rootdir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
	#app.config['SECRET_KEY'] = "I-am-Unguessable"
	SECRET_KEY = os.environ.get('SECRET_KEY') or "I-am-Unguessable"
	SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
		'sqlite:///' + os.path.join(rootdir, 'app.db')
	# track changes in object
	SQLALCHEMY_TRACK_MODIFICATION = False
	MAIL_SERVER = os.environ.get('MAIL_SERVER')
	MAIL_PORT = (os.environ.get('MAIL_PORT') or 25)
	MAIL_USE_TLS = os.environ.get("MAIL_USE_TLS") is not None
	MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
	MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
	ADMINS = ['hiesagar@gmail.com']
	POSTS_PER_PAGE = 5
