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
    events = db.relationship('Events', backref='user', lazy=True)

    def __init__(self, username, email):
        self.username = username
        self.email = email

    def set_password(self, password):
        self.password = bcrypt.generate_password_hash(password).decode('utf-8')

    def check_password(self, password):
        return bcrypt.check_password_hash(self.password, password)


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

#event list for calendar
class Events(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    event = db.Column(db.String(50))
    day = db.Column(db.Date)
    
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

#database variables for project hours
class Projects(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    completed_proj = db.Column(db.Integer)
    uncompleted_proj = db.Column(db.Integer)

    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
