from app import app, db
from app.models import User, Post

@app.shell_context_processor
def make_shell_context():
	'''
	for invoking user and post alongside app when running flask shell
	Alternative to
	>>> from app import db
	
	>>> flask shell
	>>> db 
	'''

	return {'db': db, 'User':User, 'Post': Post}