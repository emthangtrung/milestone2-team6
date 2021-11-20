
from myapp import myapp_obj
from myapp.forms import LoginForm
from flask import render_template



@myapp_obj.route("/")
def home():
    return render_template("home.html")


@myapp_obj.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()

    return render_template("login.html", form=form)