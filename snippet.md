# flask run

# flask db init
## set up migration repository
- requires flask app set as configuration variable
- create new migration directory for database migration
- has python script that describe changes to database schema

# flask db migrate -m "create user table"


# flask db downgrade
# flask db upgrade


# flask db history
# flask db current


from app import db
from app.models import User, Post
u = User(username = 'John', email = 'john@example.com')
db.session.add(u)
db.session.commit()

users = User.query.all()
for u in users:
	print(u.id, u.username, u.email)


>>> from app import db
>>> db.create_all()
>>> from app.models import User
>>> u = User(username='sagar', email='sagar@gmail.com')
>>> u.set_password('sagar')
>>> db.session.add(u)
>>> db.session.commit()

# dont show user the feed unless they login\
`in init.py`
>>> login = LoginManager(app)
>>>login.login_view = 'login'


>>> from hashlib import md5
>>> md5(b'john@doe.com').hexdigest()
'6a6c19fea4a3676970167ce51f39e6ee'
>>> http://www.gravatar.com/avatar/6a6c19fea4a3676970167ce51f39e6ee
>>> http://www.gravatar.com/avatar/6a6c19fea4a3676970167ce51f39e6ee?d=identicon&s=256

# restarting surver and console in error page
>>> set FLASK_DEBUG = 1


python -m smtpd -n -c DebuggingServer localhost:8025

(askwall) C:\Users\HP>set MAIL_SERVER=localhost

(askwall) C:\Users\HP>set MAIL_PORT = 8025