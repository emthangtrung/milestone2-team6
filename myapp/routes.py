from flask.templating import render_template_string
from myapp import myapp_obj
from myapp.forms import LoginForm
from flask import render_template, flash, redirect

from myapp import db
from myapp.models import User, Post
from flask_login import current_user, login_user, logout_user, login_required

@myapp_obj.route("/")
def home():
    

    return render_template('base.html')

@myapp_obj.route("/login")
@myapp_obj.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Login invalid username or password!')
            return redirect('/login')
        login_user(user, remember=form.remember_me.data)
        flash(f'Login requested for user {form.username.data},remember_me={form.remember_me.data}')
        flash(f'Login password {form.password.data}')
        return redirect('/')
    return render_template("login.html", form=form)