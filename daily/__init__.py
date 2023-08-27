from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///daily.db'
app.config['SECRET_KEY'] = "2aa6174651ea12849f0307e8"
db = SQLAlchemy(app)

from daily import routes