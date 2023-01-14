from flask_login import UserMixin

from blog.app import db


class User(db.Model, UserMixin):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255), unique=True)
    password = db.Column(db.String(255))
    article_id=db.relationship('Article')

    def __init__(self, email, password):
        self.email = email
        self.password = password

class Article(db.Model):
    __tablename__ = 'articles'

    id = db.Column(db.Integer, primary_key=True)
    title=db.Column(db.String(255))
    text=db.Column(db.String)
    author_id=db.Column(db.Integer, db.ForeignKey('users.id')) 