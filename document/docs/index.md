# Welcome to StudyHub - Team 6

## Installation

* `source [name of environment]/bin/activate` - Activiate your environment
* `pip install -r requirements.txt` - Install those requirement which need to run 
* `python3 run.py` -  run the application
* `pip install Flask-WkHTMLtoPDF` or via website `https://wkhtmltopdf.org/downloads.html`

## Project layout

    Readme.md              # read me file
    Specification.md       # a usecase description which is from milestone 1
    requirements.txt       # requirements which is needed to install
    create_db.py           # create db
    run.py                 # run the application
    gantt.xlsx             # Grantt Chart
    myapp/
        __init__.py        			# initialiazation code
        forms.py  				# Basic element that lets users interact with our web application
        models.py 				# Database models and everything related to it
        routes.py 				# Function decorators for application as URLs
	templates/ #html templates
		base.html      			# Starting page
		home.html      			# Home page after sign in succesfully
		register.html  			# Register page for who haven't have an account
		login.html     			# Page for user login
		input-flash-cards.html 		# Page to input and delete flashcards
		promorodo.html
		todolist.html
        download.html           # Convert html file to pdf
		renderFlashCard.html    # Convert md file to html
    document/	         # mkdocs document
	docs/
		index.md  		# The document home page
	mkdocs.yml			# mkdocs config

