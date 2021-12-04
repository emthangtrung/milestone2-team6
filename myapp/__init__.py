from flask import Flask
import os
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, login_manager
from flask_bcrypt import Bcrypt
from flask_session import Session

# gives current directory of this file
basedir = os.path.abspath(os.path.dirname(__file__))
# instance of the Flask class
myapp_obj = Flask(__name__)

myapp_obj.config["UPLOAD_FOLDER"] = "uploads"

myapp_obj.config['SECRET_KEY'] = 'secret'
myapp_obj.config['SESSION_TYPE'] = 'filesystem'
Session(myapp_obj)

myapp_obj.config['SECRET_KEY'] = '6LeIxAcTAAAAAGG-vFI1TnRWxMZNFuojJ4WifJWe'

myapp_obj.config.from_mapping(
    SECRET_KEY = 'milestone2team6',
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db'),
    SQLALCHEMY_TRACK_MODIFICATIONS = False
)



db = SQLAlchemy(myapp_obj) # Initialize flask SQLAlchemy instance
login_manager = LoginManager(myapp_obj)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'

bcrypt = Bcrypt(myapp_obj)

# making the database for the flash cards
def _update_db(obj):
    db.session.add(obj)
    db.session.commit()
    return obj
from myapp import routes, models



