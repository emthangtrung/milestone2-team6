#from flask.templating import render_template_string
from myapp import myapp_obj
from myapp.forms import LoginForm
from flask import render_template,flash,redirect

from myapp import db
#from myapp.models import Post
#from flask_login import current_user, login_user, logout_user, login_required

@myapp_obj.route("/")
def home():
    

    return render_template("home.html")


@myapp_obj.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()

    return render_template("login.html", form=form)