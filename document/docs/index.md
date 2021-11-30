# Welcome to StudyHub - Team 6

[Team's Repo](https://github.com/emthangtrung/milestone2-team6) 

## Installation

* `source [name of environment]/bin/activate` - Activiate your environment
* `pip install -r requirements.txt` - Install those requirement which need to run 
* `pip install Flask-WkHTMLtoPDF` or via website `https://wkhtmltopdf.org/downloads.html`
* `python3 run.py` -  run the application 

## Project layout

    Readme.md						# read me file
    Specification.md				# a usecase description which is from milestone 1
    requirements.txt				# requirements which is needed to install
    create_db.py					# create db
    run.py   						# run the application
    gantt.xlsx						# Grantt Chart
    myapp/
        __init__.py					# initialiazation code
        forms.py					# Basic element that lets users interact with our web application
        models.py					# Database models and everything related to it
        routes.py					# Function decorators for application as URLs
	templates/   					# html templates
		base.html   				# Starting page
		home.html   				# Home page after sign in succesfully
		register.html				# Register page for who haven't have an account
		login.html  				# Page for user login
		input-flash-cards.html 		# Page for user input and delte flashcards
		promorodo.html				# Page for user count time	
		todolist.html				# Page for user track their time
		renderFlashcard.html 		# Page for user plaint text formating
		download.html				# Page for user convert & download
		Viewcalendar2.html			# Page for user view and track calendar
		createEvents.html			# Page for user create events
	
    document/						# mkdocs document
	docs/
		index.md 					# The document home page
		classandfunction.md 		# The summary page
	mkdocs.yml 						# mkdocs config

