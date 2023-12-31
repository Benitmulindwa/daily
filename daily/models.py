from daily import db,app, login_manager
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

class User(db.Model, UserMixin):

    __tablename__="users"

    id = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.String(30), nullable=False, unique=True)
    email = db.Column(db.String(50), nullable=False, unique=True)
    password = db.Column(db.String(60), nullable=False)
    posts = db.relationship('Post', backref='users', lazy=True)



class Post(db.Model):

    __tablename__="posts"

    id = db.Column(db.Integer(), primary_key=True)
    title = db.Column(db.String(50), nullable=False, unique=True)
    body = db.Column(db.String(1024), nullable=False, unique=True)
    user_id = db.Column(db.Integer(), db.ForeignKey('users.id'), nullable=False)


with app.app_context():
    db.create_all()
