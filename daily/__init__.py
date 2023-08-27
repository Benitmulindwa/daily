from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///daily.db'
app.config['SECRET_KEY'] = "2aa6174651ea12849f0307e8"
db = SQLAlchemy(app)
bcrypt=Bcrypt(app)
login_manager = LoginManager(app)

from daily import routes