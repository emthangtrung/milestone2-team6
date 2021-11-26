from myapp import db, login_manager, bcrypt
from sqlalchemy.orm import backref
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(80), unique=True)
    password = db.Column(db.String(80))
    flashcards = db.relationship('FlashCard', backref='user', lazy=True)

    def __init__(self, username, email):
        self.username = username
        self.email = email

    def set_password(self, password):
        self.password = bcrypt.generate_password_hash(password).decode('utf-8')

    def check_password(self, password):
        return bcrypt.check_password_hash(self.password, password)


class MDfile(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    mdfile_db = db.Column(db.String(800))

    def __init__(self, mdfile_db):
        self.mdfile_db = mdfile_db

class FlashCard(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    front = db.Column(db.Text)
    back = db.Column(db.Text)

    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

#to do list db
class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    complete = db.Column(db.Boolean)

