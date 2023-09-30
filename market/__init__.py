from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///MarketData6.db'
app.config['SECRET_KEY'] = 'c0f5d23e2ef94421880ad161'

db=SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)


from market import routes