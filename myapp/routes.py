
from flask.templating import render_template_string
from werkzeug.wrappers import response
from myapp import myapp_obj
from myapp.forms import LoginForm
from flask import Flask, render_template, request, redirect, url_for
from myapp import db
from myapp.models import Todo
from datetime import datetime, date, timedelta

# import for render markdown
import markdown
import markdown.extensions.fenced_code
import markdown.extensions.codehilite
from pygments.formatters import HtmlFormatter

# create pdf to print
from flask import make_response
import pdfkit

#home page
@myapp_obj.route("/")
def home():
    return render_template("home.html")

#start login page
@myapp_obj.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    return render_template("login.html", form=form)
#end login page




# start render Markdown page
@myapp_obj.route("/renderFlashCard")
def renderFlashCard():
    return render_template("renderFlashCard.html")
@myapp_obj.route("/convert", methods=["POST"])
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
# end render Markdown page ----------------------------------------------->

# create pdf to print
@myapp_obj.route("/download")
def orders():
    return render_template("download.html")
@myapp_obj.route("/dir", methods=["POST"])
def dlPdf():
    path_wkhtmltopdf = r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe'
    html = render_template("download.html")
    config = pdfkit.configuration(wkhtmltopdf=path_wkhtmltopdf)
    pdf = pdfkit.from_string(html, False, configuration=config)
    response = make_response(pdf)
    response.headers["Content-Type"] = "application/pdf"
    response.headers["Content-Disposition"] = "inline; filename=output.pdf"
    return response
# end create pdf to print

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