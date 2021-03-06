import os
from flask.templating import render_template_string
from myapp import myapp_obj, db
from .forms import LoginForm, SignupForm, FlashCardForm, EventsForm, ProjectsForm
from .models import User, Todo, FlashCard, Events, Projects
from flask import url_for, render_template, redirect, request, flash, abort, session
from flask_login import login_user, current_user, logout_user, login_required
from sqlalchemy import exc
from datetime import datetime, date, timedelta
from flask_socketio import SocketIO, join_room, leave_room, emit


# import for render markdown
import markdown
import markdown.extensions.fenced_code
from pygments.formatters import HtmlFormatter
from werkzeug.utils import secure_filename
# import for pdf to print
from flask import make_response
import pdfkit

basedir = os.path.abspath(os.path.dirname(__file__))
# Home
@myapp_obj.route('/', methods=['GET'])
def home():
    """
    Return:
	    home page if user logged in 
    """
    return render_template('home.html')

# Signup
@myapp_obj.route('/signup', methods=['GET', 'POST'])
def signup():
    """
    Navigate to sign up page

    Returns:
	  redirecting back to the login page
    """
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
    """
    Navigate to log in page

    Returns:
	    redirecting back to the page
    """
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
    """
    Log out and redirect back to the login page

    Returns:
        redirecting back to the log in page
    """
    logout_user()
    return redirect(url_for('home'))
# Input FlashCards
@myapp_obj.route("/input-flashcards", methods=['GET', 'POST'])
@login_required
def input_flashcards():
    """
    This function will help user add flashcard

    Return:
	    redirecting back to the input flashcard page
    """
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
    """
    This function will help user delete the flash card which is inputed by user

    Return:
	    redirecting back to the input flashcard page
    """
    flashcard = FlashCard.query.get_or_404(id)
    if flashcard.user != current_user:
        abort(403)
    db.session.delete(flashcard)
    db.session.commit()
    flash('Flash card has been deleted!', 'success')
    return redirect(url_for('input_flashcards'))

# start render Markdown page
@myapp_obj.route("/renderFlashCard")
def renderFlashCard():
    return render_template("renderFlashCard.html")
@myapp_obj.route("/convert", methods=["POST"])
def renderMarkdown():
    """
    [This methods is taking markdown file and convert it into html ]

    Returns:
        [HTML file]: [convert from markdown file to html file]
    """
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
#end render Markdown page ----------------------------------------------->

#start todo list page
@myapp_obj.route("/todolist")
def todoList():
    """
    This function help user add todo list

    Returns:
        their task list with complete button
        
    """
    todo_list = Todo.query.all()
    return render_template("todolist.html", todo_list=todo_list)

@myapp_obj.route("/add", methods=["POST"])
def add():
    """Add event to data base

    Returns:
        back to todolist page
    """
    title = request.form.get("title")
    new_todo = Todo(title=title, complete=False)
    db.session.add(new_todo)
    db.session.commit()
    return redirect(url_for("todoList"))

@myapp_obj.route("/update/<int:todo_id>")
def update(todo_id):
    """Update event to data base
    
    Returns:
        back to todolist page
    """
    todo = Todo.query.filter_by(id=todo_id).first()
    todo.complete = not todo.complete
    db.session.commit()
    return redirect(url_for("todoList"))

@myapp_obj.route("/delete/<int:todo_id>")
def delete(todo_id):
    """Delete event from data base

    Returns:
        back to todolist page
    """
    todo = Todo.query.filter_by(id=todo_id).first()
    db.session.delete(todo)
    db.session.commit()
    return redirect(url_for("todoList"))
#end todo list page


#start pomorodo timer page
@myapp_obj.route("/pomorodo")
def timer():
    """
    This function help user start studying time

    Returns:
        25mins countdown
        
    """
    return render_template("pomorodo.html")
#end pomorodo timer page

# create pdf to print
@myapp_obj.route("/download")
def orders():
    return render_template("download.html")
@myapp_obj.route("/dir", methods=["POST"])
def dlPdf():
    """
    [This function is taking an html file and 
        convert it into pdf. Download available]

    Returns:
        [Pdf file]: [a pdf file with button to download]
    """
    # add wkhtmltopdf local path when download wkhtmltopdf from its website
    path_wkhtmltopdf = r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe'
    # read html file
    html = render_template("download.html")
    # convert to pdf
    config = pdfkit.configuration(wkhtmltopdf=path_wkhtmltopdf)
    pdf = pdfkit.from_string(html, False, configuration=config)
    # return pdf file
    response = make_response(pdf)
    response.headers["Content-Type"] = "application/pdf"
    response.headers["Content-Disposition"] = "inline; filename=output.pdf"
    return response


#adding evetns to calendar
@myapp_obj.route("/create-event", methods=['GET','POST'])
@login_required
def create_event():
    """user can add a event on specific date. 
        The event gets saved onto the data base

    Returns:
        lets user know their event has been added. 
        Button is shown so user can go to calender.
        Show their event block on the calender
    """
    form = EventsForm()
    user_events = Events.query.filter_by(user=current_user).all()
    if form.validate_on_submit():
        new_event = Events(event=form.event.data, day=form.day.data,user=current_user)
        db.session.add(new_event)
        db.session.commit()
        flash('Event has been added')
        return redirect(url_for('create_event'))
    return render_template("createEvents.html", form=form, user_events=user_events)
    return(user_events)
#viewing calendar
@myapp_obj.route("/calendar-view", methods=['GET', 'POST'])
@login_required
def calender_view():

    """user can see their event block on the calendar once they have made one

    Returns:
        back to viewCalendarV2 page
    """
    events = Events.query.all()
    return render_template("viewCalendarV2.html", events = events)


# Chat room section
socketio = SocketIO(myapp_obj, manage_session=False)
@myapp_obj.route('/chatRoom', methods=['GET', 'POST'])
def index():
    """[This function is to return to chatRoom.html]

    Returns:
        [Template]: [chatRoom.html]
    """    
    return render_template('chatRoom.html')
# Post method
@myapp_obj.route('/chat', methods=['GET', 'POST'])
def chat():
    """[Get POST method from user and store data in session]

    Returns:
        [data]: [Return to chat.html]
    """    
    if(request.method=='POST'):
        username = request.form['username']
        room = request.form['room']
        session['username'] = username
        session['room'] = room
        return render_template('chat.html', session = session)
    else:
        if(session.get('username') is not None):
            return render_template('chat.html', session = session)
        else:
            return redirect(url_for('index'))
# Display message
@socketio.on('join', namespace='/chat')
def join(message):
    """[Display message]

    Args:
        message ([string]): [output message]
    """    
    room = session.get('room')
    join_room(room)
    emit('status', {'msg':  session.get('username') + ' has entered the room!'}, room=room)

@socketio.on('text', namespace='/chat')
def text(message):
    """[Get the room data]

    Args:
        message ([string]): [Display room]
    """    
    room = session.get('room')
    emit('message', {'msg': session.get('username') + ' : ' + message['msg']}, room=room)

@socketio.on('left', namespace='/chat')
def left(message):
    """[Display message when user left the room]

    Args:
        message ([string]): [Display message]
    """    
    room = session.get('room')
    username = session.get('username')
    leave_room(room)
    session.clear()
    emit('status', {'msg': username + ' has left the room.'}, room=room)
# end chat room section -------------------------------------------------------->
# print all flashcards
@myapp_obj.route('/print-all-flashcards/')
@login_required
def print_all_flashcards():

    '''
    It retrieves all the flashcards for the logged in user and prints it to pdf

    Returns:
            pdf file with the all flashcards for the logged in user
    '''
    user_flashcards = FlashCard.query.filter_by(user=current_user).all()
    html = render_template('allFlashcards.html', user_flashcards=user_flashcards)

    return convert_to_pdf(html)

# print a single flashcard
@myapp_obj.route('/print-single-flashcard/<int:id>')
@login_required
def print_single_flashcard(id):

    '''
    It retrieves a flashcard with given id for the logged in user and prints it to pdf format

    Returns:
            pdf file with the single flashcard
    '''
    flashcard = FlashCard.query.get_or_404(id)
    if flashcard.user != current_user:
        abort(403)
    html = render_template('singleFlashcard.html', flashcard=flashcard)

    return convert_to_pdf(html)

# convert flashcard to pdf to print
def convert_to_pdf(html):

    '''
    This function takes the html page as an input and returns a pdf format file for downloading

    Returns:
            A pdf file with one or multiple pages containing flashcards
    '''
    pdf = pdfkit.from_string(html, False)
    response = make_response(pdf)
    response.headers["Content-Type"] = "application/pdf"
    response.headers["Content-Disposition"] = "inline; filename=flashcard.pdf"
    return response

#makes a graph for the user so they can vizually see their hours worked
@myapp_obj.route('/view-hours-worked', methods=['GET', 'POST'])
@login_required
def hours_worked():
    """User can add amount of hours worked on a project and hours needed to be completed
       The hours get saved onto the database

    Returns:
       Lets the user know that the hours have been added. Gets redirected to the page.
       Once redirected the graph updates
    """   

    form = ProjectsForm()
    user_projects = Projects.query.filter_by(user=current_user).all()
    if form.validate_on_submit():
        time_worked = Projects(dateStart=form.dateStart.data, dateEnd=form.dateEnd.data, user = current_user)
        names_worked = Projects(nameOfCase=form.nameOfCase.data, nameOfPerson=form.nameOfPerson.data, user = current_user)
        db.session.add(time_worked)
        db.session.add(names_worked)
        db.session.commit()
        flash('Your Hours Have Been Added')
        return redirect(url_for('hours_worked'))
    return render_template('projectsGraph.html', form=form, user_projects=user_projects)

@myapp_obj.route("/splash")
def splashpage():
    return render_template("splash.html")

