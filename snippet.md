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