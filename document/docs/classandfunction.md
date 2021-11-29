
# Summary  



## **Summary of classes and functions**


#### forms.py

###### Form Class:

* [LoginForm](#loginform)
* [SignupForm](#signupform)
* [FlashCardForm](#flashcardform)

#### models.py

###### Model Class:

* [User](#user)
    * [__init__()](#init)
    * [set_password()](#set_password)
    * [check_password()](#check_password)
* [Flashcard](#flashcard)
* [Todo](#todo)

#### routes.py

###### Functions:
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

#### forms.py:

###### SignupForm

```
a form which user use to fill out to sign up

Username(str)   a string field indicate username
Email(str)	a string field indicate email
Password(str)	a string field indicate password
Submit		a string field triggered when user submit

```


###### LoginForm

```
a form which users use to fill out to login

Username (str)  a string field indicate username
Password (str)	a string field indicate password
Submit		a string field triggered when user submit

```

###### FlashCardForm

```
a form which user use to input flash card

Front (str)	a string field indicate input of front of flash card	
Back (str)      a string field indicate input of back of flash card
Submit		a string field triggered when user submit to create a new flash card

```


#### models.py:

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

self (obj)              reference to this class instance
username(str)		a string which contain username
email                   a string which contain email

```

###### set_password

```
set password by using bcrypt hashing

self (obj)              reference to this class instance
password (string)       a string which contain password

```

###### check_password

```
check password by using bcrypt hashing

self (obj)             reference to this class instance
password (string)      a string which contain password

The function returns True if the password provided by the user matches the hash, or False otherwise

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


#### routes.py

##### function:


###### home
```

```
###### signup

```

```
###### login
```

```
###### logout
```

```
###### input_flashcard
```

```
###### delete_flashcard
```

```
###### renderMarkdown
```

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
```


# Summary

#### **forms.py**



#### **models.py**



#### **routes.py**


