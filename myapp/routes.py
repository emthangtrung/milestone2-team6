import os
from flask.templating import render_template_string
from myapp import myapp_obj, db
from .forms import LoginForm, SignupForm, FlashCardForm
from .models import User, MDfile, Todo, FlashCard
from flask import url_for, render_template, redirect, request, flash, abort
from flask_login import login_user, current_user, logout_user, login_required
from sqlalchemy import exc
from datetime import datetime, date, timedelta

# import for render markdown
import markdown
import markdown.extensions.fenced_code
from pygments.formatters import HtmlFormatter
from werkzeug.utils import secure_filename


basedir = os.path.abspath(os.path.dirname(__file__))
# Home
@myapp_obj.route('/', methods=['GET'])
def home():
    return render_template('home.html')

# Signup
@myapp_obj.route('/signup', methods=['GET', 'POST'])
def signup():
    form = SignupForm()
    # Check if the form is validated on submission
    if form.validate_on_submit():
        # Check if the user is already there
        user = User.query.filter_by(username=form.username.data).first()
        if user is None:
            user = User.query.filter_by(email=form.email.data).first()
            if user is None: # Check if email is already registered

                user = User(
                    username=form.username.data,
                    email=form.email.data,
                )

                user.set_password(form.password.data)

                db.session.add(user)
                db.session.commit()
                flash('Registration Successful! You can now log in', 'success')
                return redirect(url_for('login'))
            else:
                flash(f'Email {form.email.data} is already registered!', 'danger')
        else:
            flash(f'Username {form.username.data} is taken!', 'danger')
    # Pass the registration form to the register.html template so we can render it on frontend
    return render_template('register.html', form=form)
# Login
@myapp_obj.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    # Check form validation
    if form.validate_on_submit():

        user = User.query.filter_by(username=form.username.data).first()
        # If the username and password are in db then log in the user
        if user and user.check_password(form.password.data):
            login_user(user)
            flash('Login Successful!', 'success')
            return redirect(url_for('input_flashcards'))
        else:
            flash('Login Unsuccessful. Please check email and password', 'danger')
    # Pass the form in the render_template function so we can render it to frontend
    return render_template('login.html', form=form)

# Logout
@myapp_obj.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for('home'))
# Input FlashCards
@myapp_obj.route("/input-flashcards", methods=['GET', 'POST'])
@login_required
def input_flashcards():
    form = FlashCardForm()
    user_flashcards = FlashCard.query.filter_by(user=current_user).all()
    if form.validate_on_submit():
        flashcard = FlashCard(front=form.front.data, back=form.back.data, user=current_user)
        db.session.add(flashcard)
        db.session.commit()
        flash('Flash Card Created Successfully', 'success')
        return redirect(url_for('input_flashcards'))
    return render_template('input-flash-cards.html', form=form, user_flashcards=user_flashcards)

# Delete FlashCards
@myapp_obj.route("/delete-flashcard/<int:id>")
@login_required
def delete_flashcard(id):
    flashcard = FlashCard.query.get_or_404(id)
    if flashcard.user != current_user:
        abort(403)
    db.session.delete(flashcard)
    db.session.commit()
    flash('Flash card has been deleted!', 'success')
    return redirect(url_for('input_flashcards'))


#start render Markdown page
# --> it is too simple
# --> still under contruction (working for more function)
def renderMarkdown():
    read_file = open("Readme.md", encoding="utf8")
    md_template_string = markdown.markdown(
          read_file.read(), extensions=["fenced_code"]
      )
    # Generate Css for syntax highlighting
    formatter = HtmlFormatter(style="emacs",full=True,cssclass="codehilite")
    css_string = formatter.get_style_defs()
    md_css_string = "<style>" + css_string + "</style>"
    md_template = md_css_string + md_template_string
    return md_template

@myapp_obj.route("/renderFlashCard")
def renderFlashCard():
    mkd_text = renderMarkdown()
    # return mkd_text
    return render_template("renderFlashCard.html", mkd_text=mkd_text)
#end render Markdown page ----------------------------------------------->

#start todo list page
@myapp_obj.route("/todolist")
def todoList():
    todo_list = Todo.query.all()
    return render_template("todolist.html", todo_list=todo_list)

@myapp_obj.route("/add", methods=["POST"])
def add():
    title = request.form.get("title")
    new_todo = Todo(title=title, complete=False)
    db.session.add(new_todo)
    db.session.commit()
    return redirect(url_for("todoList"))

@myapp_obj.route("/update/<int:todo_id>")
def update(todo_id):
    todo = Todo.query.filter_by(id=todo_id).first()
    todo.complete = not todo.complete
    db.session.commit()
    return redirect(url_for("todoList"))

@myapp_obj.route("/delete/<int:todo_id>")
def delete(todo_id):
    todo = Todo.query.filter_by(id=todo_id).first()
    db.session.delete(todo)
    db.session.commit()
    return redirect(url_for("todoList"))
#end todo list page


#start pomorodo timer page
@myapp_obj.route("/pomorodo")
def timer():
    return render_template("pomorodo.html")
#end pomorodo timer page
