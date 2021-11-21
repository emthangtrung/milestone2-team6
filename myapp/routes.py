from flask.templating import render_template_string
from myapp import myapp_obj
from myapp.forms import LoginForm
from flask import Flask, render_template, request, redirect, url_for
from myapp import db
from myapp.models import Todo

# import for render markdown
import markdown
import markdown.extensions.fenced_code
from flask.ext.markdown import Markdown

@myapp_obj.route("/")
def home():
    return render_template("home.html")


@myapp_obj.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    return render_template("login.html", form=form)

# Render Markdown page
def renderMarkdown():
    read_file = open("Specification.md", "r")
    md_template_string = markdown.markdown(
          read_file.read(), extensions=["fenced_code"]
      )
    return md_template_string
Markdown(myapp_obj)
@myapp_obj.route("/renderFlashCard")
def renderFlashCard():
    mkd_text = renderMarkdown()
    return render_template("renderFlashCard.html", mkd_text=mkd_text)

    
#todo list page
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


#pomorodo timer page
@myapp_obj.route("/pomorodo")
def timer():
    return render_template("todolist.html")