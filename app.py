from app import app, db
from app.models import User, Post

@app.shell_context_processor
def make_shell_context():
	'''
	for invoking user and post alongside app when running flask shell
	# https://stackoverflow.com/questions/51337758/app-shell-context-processor-decorator-does-not-register-the-function-as-a-shell
	>>> flask shell
	>>> db 
	'''

	return {'db': db, 'User':User, 'Post': Post}