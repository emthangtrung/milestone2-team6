
# Summary  



## **Summary of classes and functions**


#### **forms.py**

* [LoginForm](#loginform)
* [SignupForm](#signupform)
* [FlashCardForm](#flashcardform)

#### **models.py**

* [User](#user)
    * [__init__()](#init)
    * [set_password()](#set_password)
    * [check_password()](#check_password)
* [Flashcard](#flashcard)
* [Todo](#todo)

#### **routes.py**

* [home()](home)
* [signup()](#signup)
* [login()](#login)
* [logout()](#logout)
* [input_flashcard()](#input_flashcard)
* [delete_flashcard()](#delete_flashcard)
* [renderMarkdown()](#renderMarkdown)
* [todoList()](#todoList)
* [add()](#add)
* [update()](#update)
* [delete()](#delete)
* [timer()](#timer)
* [dlPdf()](#dlPdf)


## **Doctrings**

#### **forms.py:**

###### SignupForm

```
a form which user use to fill out to sign up

username (str)		string field indicate username
email (str)		string field indicate email 
password (str)		string field indicate password
Submit			trigger when user submit


```

###### LoginForm

```
a form which users use to fill out to login

username (str)		string filed indicate username 
password (str)		string field indicate password 
submit			trigger when user submit

```

###### FlashCardForm

```
a form which user use to input flash card

front (str)		string field indicate input of front of flash card	
back (str)		string field indicate input of back of flash card
submib			trigger when user submit to create a new flash card

```


#### **models.py:**

###### Users

```
information of user

id (int)                integer indicate id of user
username (str)          string indicate username
email   (str)           string indicate email 
password (str)          string indicate password
flashcard (List<obj>)   list of object containing flashcards which is added by the user

```

###### init

```
Initialize the user

self (obj)		reference to this class instance
username(str)		string which contain username
email(str)		string which contain email

```

###### set_password

```
set password by using bcrypt hashing

self (obj)              reference to this class instance
password (string)       string which contain password

```

###### check_password

```
check password by using bcrypt hashing

self (obj)             reference to this class instance
password (string)      string which contain password

Returns: 
	True if the password provided by the user matches the hash, or False otherwise

```

###### flashcard

```
flashcard which is add by user

id (int)               id integer of the flashcard
front (str)            string of the front of flashcard
back (str)             string of the back of flashcard
user_id (int)          id interger of the users's card

```


###### todo
```


```


#### **routes.py**

##### function:


###### home
```
Return:
	home page if user logged in 

```

###### signup
```
Navigate to sign up page 
    
Returns:
	  redirecting back to the login page

```
###### login
```
Navigate to log in page 
 
Returns:
	  redirecting back to the page
     or 
	  redirecting to input flashcard page

```
###### logout
```
Log out and redirect back to the login page
         
Returns:
        redirecting back to the log in page

```

###### input_flashcard
```
This function will help user add flashcard

Return:
	redirecting back to the input flashcard page

```
###### delete_flashcard
```
This function will help user delete the flash card which is inputed by user

Return:
	redirecting back to the input flashcard page

```
###### renderMarkdown
``` 
"""
[This methods is taking markdown file and convert it into html ]

Returns:
    [HTML file]: [convert from markdown file to html file]
"""
```
###### todoList
```

```
###### add
```

```
###### update
```

```
###### delete
```

```
###### timer
```

```
###### dlPdf
```
"""
[This function is taking an html file and 
    convert it into pdf. Download available]

Returns:
    [Pdf file]: [a pdf file with button to download]
"""
```


# Summary

#### **forms.py**



#### **models.py**



#### **routes.py**


