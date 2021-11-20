
from myapp import myapp_obj
from myapp.forms import LoginForm
from flask import render_template

# ------------Render Markdown work in process ---------------->
# import for render markdown

# import markdown
# import markdown.extensions.fenced_code
# from flaskext.markdown import Markdown
# # pdf download able
# from flask import make_response
# import pdfkit
# ---------------------------------------------->



# Home Page
@myapp_obj.route("/") 
def home():
    return render_template("home.html")
# Login Page
@myapp_obj.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    return render_template("login.html", form=form)








# ------------Render Markdown work in process ---------------->
# Render Markdown
def renderMarkdown():
    read_file = open("Specification.md", "r")
    md_template_string = markdown.markdown(
          read_file.read(), extensions=["fenced_code"]
      )
    return md_template_string
# Markdown(myapp_obj)
# @myapp_obj.route()
def renderFlashCard():
    mkd_text = renderMarkdown()
    return render_template("renderFlashCard.html", mkd_text=mkd_text)

    # pdf = pdfkit.from_string(html, False)
    # response = make_response(pdf)
    # response.headers["Content-Type"] = "application/pdf"
    # response.headers["Content-Disposition"] = "inline; filename=output.pdf"
    # return response
# ------------------------------------------------------------------------------>
