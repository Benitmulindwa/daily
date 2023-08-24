from flask import Flask, render_template
import requests
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///daily.db'
db = SQLAlchemy(app)


class User(db.Model):
  __tablename__ = 'users'
  id = db.Column(db.Integer(), primary_key=True)
  username = db.Column(db.String(30), nullable=False, unique=True)
  email = db.Column(db.String(50), nullable=False, unique=True)
  password = db.Column(db.String(60), nullable=False)


with app.app_context():
  db.create_all()
  user1 = User(username="john",
               email="exam@gmail.com",
               password="123456789")
  db.session.add(user1)
  db.session.commit()
  print(User.query.all())
  pass
#print(user1.username)

@app.route("/")
def home():
  response = requests.get("https://api.npoint.io/b26898f9241e01f827c6")
  data = response.json()
  return render_template("index.html", posts=data)


@app.route("/post/<int:id>")
def blog(id):
  response = requests.get("https://api.npoint.io/b26898f9241e01f827c6")
  data = response.json()
  return render_template("post.html", post=data[id - 1])


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
