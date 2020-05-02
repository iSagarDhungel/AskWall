from flask import *
from flask_sqlalchemy import SQLAlchemy 
from datetime import datetime


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///askwall_db.db'
db = SQLAlchemy(app)

class User(db.Model):
	id = db.Column(db.Integer, primary_key = True, unique=True)
	username = db.Column(db.String(100), nullable=False, unique = True)
	email = db.Column(db.String(120), nullable= False, unique = True)
	password = db.Column(db.String(120), nullable = False)
	date_created = db.Column(db.DateTime, default=datetime.utcnow)

@app.route('/')
def index():
	return render_template('index.html')

if __name__ == "__main__":
	app.run(debug=True)

