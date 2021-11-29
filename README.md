**Milestone2-team6**

Project github repo: https://github.com/emthangtrung/milestone2-team6.git

Danh Pham([emthangtrung (github.com)](https://github.com/emthangtrung))

[![StudyHub.jpg](https://i.postimg.cc/zf0ny6vD/StudyHub.jpg)]()

#### Member name:

Danh Pham (https://github.com/emthangtrung)

Ngoc Tran (https://github.com/ntran12)

Ulises Duran (https://github.com/UJDuran)

Thinh Vo (https://github.com/kiemkhach2020)

#### Main Github repo:

https://github.com/emthangtrung/milestone2-team6

## Use Case #1: Create an Account

**Date:** 09/15/2021

**Product Name:** Study Hub

**Problem Statement:** Help users log in to use the app

**Non-functional Requirements:** Confirmation Emails should be sent within 1 hours.

**Use Case Name:** Create an Account

##### Actors
- Everyone

##### Preconditions
- New User
- Have email account to sign up.

##### Triggers
- New user clicks on option “Join us”

##### Primary Sequence
1.	New users click on option “Join us”.
2.	New users fill out some information such as first name, last name, date of birth, sex.
3.	New users create their username .
4.	System checks the username is available or not.
5.	New users create their own password.
6.	System check password meet the requirement or not.
7.	New users enter their email.
8.	System check email was used or not.
9.	New users click summit option at the end of platform.
10.	System creates a new user. 
11.	System sends a confirmation email to the user’s email.

##### Primary Postconditions
- Users can log in to use the app.

##### Alternate Triggers
- Users enter information in section where the system displays error again until the system does not display error message

##### Alternate Sequences
Username which user enter, was used.
- The system displays an error message to the user.
- The system prompt user to enter a valid username.

Password which user enter, does not meet the requirement
- The system displays an error message to the user.
- The system prompt user to enter a valid password.

Email which user enter, was used
- The system displays an error message to the user.
- The system prompts user to enter a different email.

##### Alternate Postconditions
- User can sign up.




## Use Case #2: Delete an Account 

**Date:** 09/15/2021

**Product Name:** Study Hub

**Problem Statement:** Help users delete an account

**Non-functional Requirements:** Respond to delete confirmation within 1 minutes.

**Use Case Name:** Delete an Account 

##### Summary
- Users can delete an account if they want.

##### Actors
- All users

##### Preconditions
- Users must have an account.

##### Triggers
- Users click on option "Delete"

##### Primary Sequence
1.	The user clicks on “setting” on menu bar.
2.	The use clicks on “delete an account”
3.	The system ask user again to confirm they want to delete an account.
4.	Users click confirm (Yes)
5.	System sends a confirmation to user’s email.

##### Primary Postconditions
- Users cannot log in to system anymore.

##### Aternate Squences
- Users click on option "Cancel"

##### Alternate Sequences
Users change their mind, or they click on delete an account by mistake.

- System prompts the user to confirm.

- User click cancel (No)

Users change their mind, or they click on delete an account by mistake.

- System prompts the user to confirm.

- User click cancel (No).


##### Alternate Postconditions
- Users still have an account to log in.




## Use Case #3: Input a markdown file and output flash cards.

**Date:** 09/15/2021 

**Product Name:** Study Hub

**Problem Statement:** Help users see and share flashcard easier

**Non-functional Requirements:** User can choose color for markdown file

**Use Case Name:** Input a markdown file and output flash cards.

##### Actors
- All users

##### Preconditions
- Users have account.
- Users must have at least one flashcard.
- Markdown file should be provide as input

##### Triggers
With input a markdown file: 

- Users input file

With output flashcard: 

- Click option “share” on the top-right of the flashcard.

##### Primary Sequence
With input markdown file:
1.	Users click option “create”
2.	System prompts 2 text boxes (front and back card) for user to fill out. 
3.	Users input a markdown file
4.	System recognizes the file
5.	System automatically make flashcard into markdown file.

With output flashcard:
1.	Users click on flashcard which users want to share.
2.	Users click option “share” on the top-right of that flashcard.
3.	System prompts some options such as download to user’s phone or share to their friends via message, Facebook, email, etc.
4.	Users click on option they choose.
5.	Users confirm by clicking download/send.

##### Primary Postconditions
With input a markdown file: 
- Make flashcard easier to read

With output flashcard: 
- Users can download their flashcard to their phone, so users can see it everywhere. Also, users can share useful information to their friends.

##### Alternate Triggers

With input a markdown file: 

- Users check the file is saved or not

With output flashcard: 
- Users turn on internet in their phone.

##### Alternate Squences
With input a markdown file: 
- System display an error message if input file is not valid.

With output flashcard: 
- Users save or share without internet

- System displays an error message to user.

- System prompts user turn on internet.

##### Alternate Postconditions
With input a markdown file:	
- Users successfully input a markdown file.

With output flashcard:

- Users successfully download/send.


## Use Case #4: Share flash cards (add to their account) 

**Date:** 09/15/2021 

**Product Name:** Study Hub

**Problem Statement:** Help users save a useful flashcard from others to their folder

**Non-functional Requirements:** Users only can save flashcard from another user when they put their flashcard in public.

**Use Case Name:** Share flash cards (add to their account) 

##### Actors
- All users

##### Preconditions
- Users have an account.

##### Triggers
- User click on heart icon on the front-right of that flashcard.

##### Primary Sequence
1.	Users choose which flashcard they want to share (save) to their account
2.	System prompts the users which folder they want to save the flashcard in
3.	Users choose folder to save in
4.	System prompts the users confirm
5.	Then users click option “Yes”
6.	System saves that flashcard to the folder which user choose

##### Primary Postconditions
- That flashcard is saved in user’s folder

##### Alternate Triggers
1.	Users click to the flashcard and hold 
2.	System prompts the user some options
3.	Users click option “delete”

##### Alternative Squences
- Users change their mind that they don’t want to save.

##### Alternate Postconditions
- Less flashcard in user's folder




## Use Case #5: Change the order of flashcards based on how often user got answer correctly

**Date:** 9/15/2021 

**Product Name:** Study Hub

**Problem Statement:** calculate the percentage of how many correct and incorrect answers

**Non-functional Requirements:** efficiency requirement

**Use Case Name:** check answers

##### Actors:
- Users

##### Preconditions:
- If answer is correct

##### Triggers:
- Flashcard to change their position automatically

##### Primary Sequence: 
1. Get answer from user
2. Check answer
3. If answer is corrected -> trigger flashcard to change
4. Else -> no change

**Primary Postconditions**: answer must be filled

##### Alternate Trigger:
- Prompt user to answer the questions

##### Alternative Sequences:
1. If answer is blank -> prompt a message
2. Else -> trigger to check answer

##### Alternate Postconditions:
- Save log



## Use Case #6: Create pdf of flash card to print

**Date:** 9/15/2021 8:10 pm 

**Product Name:** Study Hub

**Problem Statement:**  a button to print

**Non-functional Requirements:** quality

**Use Case Name:** create pdf file

##### Actors:
- users

##### Preconditions:
- a "Print" button

##### Triggers:
-  create pdf method


##### Primary Sequence: 
1. when button is clicked -> trigger to print

##### Primary Postconditions:
- answer can be filled or unfilled

##### Alternate Trigger:
- prompt user to [Yes] to print [No] to cancel

##### Alternative Sequences: 
1. if button is clicked -> prompt a message
2. if user choose [Yes] -> trigger to print
3. else -> trigger to cancel

##### Alternate Postconditions:
- end case: go back to home





## Use Case #7: Mind map of flash cards

**Date:** 9/15/2021

**Product Name:** Study Hub

**Problem Statement:** Creative solutions to problems

**Non-functional Requirements:** Useability

**Use Case Name:** Creative Solutions

##### Actors:
- user

##### Preconditions:
- Flashcards

##### Triggers:
- Solution for each flashcard
- A chat box with tutor

##### Primary Sequence:
1. Select the best study subject
2. Find study resources
3. Search questions by multiple types
4. Ask tutors for help
5. Practice

**Primary Postconditions**

- Help users learn from flash cards 

##### Alternate Trigger:
1. a search box
2. a filter
3. a chat box
4. email box

##### Alternative Sequences:
1. if user click search -> trigger a filter
2. find best match materials word by word
3. if problem not found -> trigger to chat box
4. find the best match tutor

##### Alternate Postconditions:
- Submit question and wait for respond





## Use Case #8 Render markdown notes

**Date:** 9/16/2021

**Product Name:** Study Hub

**Problem Statement:** Plaint text formatting

**Non-functional Requirements:** Quality

**Use Case Name:** Markdown

##### Actors:
- users

##### Preconditions:
- software testing

##### Triggers:
- pdf, html, docx, xml, etc..

##### Primary Sequence:
1. a design
2. content    
3. domain
4. create the site
5. search engines
6. launch

**Primary Postconditions**:

- Good design

##### Alternate Trigger:
- export to Docx, pdf, html, etc.

##### Alternative Sequences:
1. add extra features
2. redesign
3. more capacity

##### Alternate Postconditions:
- add many functions as needed





## Use Case #9: Converts marked down notes to pdf 

**Date:** 09-15-2021 

**Product Name:** Study Hub

**Problem Statement:**

**Non-functional Requirements:**

**Use Case Name:** Converts marked down notes to pdf 

##### Actors
- User

##### Preconditions
- Notes must exist (either from another user or ther own)
- Notes must me marked

##### Triggers
- User clicks on "Conver to PDF"

##### Primary Sequence
1. User confrims the pdf conversion
2. System asks user to pick a destination for PDF
3. User picks destination for PDF
4. Message displays that file has been downloaded

**Primary Postconditions:**

- Pdf has been created in users desired destination

##### Alternate Trigger
- User clicks on "Print" button when asked to convert to pdf

##### Alternative Sequences
1. User confirms the pdf 
2. User has an option to print instead of saving
3. User picks printer destination
4. Message displays that file has been printed

##### Alternate Postconditions
- A hard copy of pdf has been printed 





## Use Case #10: Create graph (nodes and edges) of connection between notes

**Date:** 09-15-2021 

**Product Name:** Study Hub

**Problem Statement:**

**Non-functional Requirements:**

**Use Case Name:** Create graph (nodes and edges) of connection between notes

##### Actors
- Notes
- User

##### Preconditions
1. Must have notes saved on their account

##### Triggers
1. User clicks on "Connections Between Notes" tab
2. User click on "New Graph"

##### Primary Sequence
1. User goes to designated tab 
2. User creates new graph by clicking "New Graph"
3. User will select notes to draw connection to eachother                                                                                                                                                        5. System will prompt user to name graph
4. User clicks on create graph                                                                                          
5. System will prompt user to name graph
6. User names and confirms it 

**Primary Postconditions**
1. A graph is created between selected notes 

##### Alternate Trigger
1. User clicks on "Connections Between Notes" tab
2. User clicks on "View graphs"

##### Alternative Sequences
1. User goes to designated graph
2. User clicks on "View Graphs"
3. User will pick a presaved graph 

##### Alternate Postconditions
1. User can view their previous saved graph




## Use Case #11: Share Notes With Other People 

**Date:** 09-15-2021 

**Product Name:** Study Hub

**Problem Statement:**

**Non-functional Requirements:**

**Use Case Name:** Share Notes With Other People 

##### Actors
- Users

##### Preconditions
1. User must have an account to share Notes 
2. User must have notes to share

##### Triggers
1. User clicks on "Share Note"

##### Primary Sequence
1. User goes to desired note they want to share
2. User clicks on "Share Notes"
3. User will confirm if they want to share

**Primary Postconditions**
1. User has shared their notes

##### Alternate Trigger
1. User clicks on "View Notes"

##### Alternative Sequences
1. User goes to desired Note
2. User clicks on "View Notes"

##### Alternate Postconditions
1. Notes must be shared either by them or another user




## Use Case #12: Quickly rename files using regular expressions

**Date:** 09-15-2021 

**Product Name:** Study Hub

**Problem Statement:**

**Non-functional Requirements:**

**Use Case Name:** Quickly rename files using regular expressions

##### Actors
- User 
- Website

##### Preconditions
- File must exist
- File cannot be renamed the same name

##### Triggers
1. User will click on the “Rename” button

##### Primary Sequence
1. User clicks on the three dot icon next to the file
2. User clicks on “Rename” button 
3. User will write the expression
4. The website will convert the expression
5. The user will confirm the conversion

**Primary Postconditions**
1. File has been renamed

##### Alternate Trigger
1. User did not type the Expression correctly

##### Alternative Sequences
1. Website will give user an error
2. User will fix error

##### Alternate Postconditions
1. File has been renamed





## Use Case #13 Create time block

**Date:** 9/15/2021

**Product Name:** Study Hub

**Problem Statement:** organize time flow 

**Actors**: User

**Preconditions:** no need 

**Triggers:** 

- Click and drag to create time block

##### Primary Sequence

1. system prompt user to create their block by drag to specific time

2. user select time to input there work and task

3. user can input what they need in time block

**Primary Postconditions**

1. User feel good with  attracted interphase 

2. Increase concentration

**Alternate Trigger:**

- User can click and drag time block to another time frame if want make change





## Use Case #14 use pomodoro timer

**Date:** 9/15/2021

**Product Name:** Study Hub

**Problem Statement:** feature that user can track there time while studying

**Non-functional Requirements:** timer can be display or non display for user

**Actors:** all user

**Preconditions:** no need so user can use it asap and no annoy

**Triggers:** 

- Timer must be input amount of time they want to remind

- Timer can be start when user hit "SPACE"

**Primary Sequence:** 

1. User input their work time and begin countdown

2. Timer automatically alert when time ran out (No need human interaction)

**Primary Postconditions:**

- User now have timer for their work and break time

**Alternate Trigger:**

- Space or click for re-timing

  



## Use Case #15 visualize time blocks

**Date:** 9/16/2021

**Product Name:** Study Hub

**Problem Statement:** help user see their time flow

**Non-functional Requirements:** 

- Able to make there scheduler private 

**Actors:** User

**Preconditions:**

- User must create time block before to see 

**Triggers:** 

- Scroll mouse to see time flow
- zoom in out for better view

**Primary Sequence:**

1. User customize their time block 

2. Always appear on screen and never sleep

**Primary Postconditions:**

1. User control their time flow

2. User now can track their schedule more easy and attractive





## Use Case #16 add to do list or tracker

**Date:** 9/16/2021

**Product Name:** Study Hub

**Problem Statement:** help user make to do list

**Non-functional Requirements:**

- tick box for job done

**Actors:** User

**Preconditions:** open to do list on the right of the app

##### Triggers:

- Click "to do list" button to open

##### Primary Sequence:

1. User input there task

2. Tick for mark as done job

**Primary Postconditions**

- User can see what they have done to keep work flow more efficient



## Use Case #17 visualize hours worked and project

**Date:** 9/16/2021

**Product Name:** Study Hub

**Problem Statement:** 

- User want to know how much time they spent on their work and project

**Non-functional Requirements:**

- graph of work times and work log

**Actors:** User, Manager

**Preconditions:** no need 

##### Triggers:

- User selects "time tracker" button

##### Primary Sequence

1. System will appear their total work time in day, week, and month

2. User select columm graph for more visuallize

**Primary Postconditions:**

1. manager can track how much time their co-worker or student spent time on

2. regular user can know how much time they spent on work



##### Alternate Trigger: 

- User click "Create .xlss file" for excel data

##### Alternative Sequences

- Export excel file 

##### Alternate Postconditions:

- Calculate salary or grade student on what they have done

  
