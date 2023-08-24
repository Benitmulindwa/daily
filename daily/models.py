from daily import db


class User(db.Model):

    id = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.String(30), nullable=False, unique=True)
    email = db.Column(db.String(50), nullable=False, unique=True)
    password = db.Column(db.String(60), nullable=False)
    posts = db.relationship('Post', backref='user', lazy=True)


class Post(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    title = db.Column(db.String(50), nullable=False, unique=True)
    body = db.Column(db.String(1024), nullable=False, unique=True)
    user_id = db.Column(db.Integer(), db.ForeignKey('user.id'), nullable=False)
