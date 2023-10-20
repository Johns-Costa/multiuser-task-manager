# Multi User Task Manager

 Multi User Task Manager for a family or small company that has the need of organizing and register their tasks.
 It is designed ir order for each user to have acces to their own set of tasks. If the tasks are to be shared a user name and pasword can be shared between user and every person involved can contribute with the tasks that have been done and add new ones.
 Multi User Task Manager  is a very useful tool for everyone that need some tasks management in their life

![am i responsive](/assets/images/amiresponsive.png)

## Design and Inspiration
------
- I was inspired to make a task manager app from feeling the need of self organization. After some thought it came to my mind it would be much more usefull to make an app that could host several users. Each user having their own login it their specific tasks. I wanted to create an application that provided each user a confortable place to store their task list, be safe and accessible from anywhere with an internet connection.
- Below is the flowchart I created as a guide when I was first visualising how the code would be represented.

![flowchart](/assets/documentation/images.webp/flowchart.webp)

ADD CHART!!!!!

## How to use
------
Through the progression of the app, the user will go through the following:
- Login with your credentials (user name and password)
- If new user you will be redirected to a create new user path
- If user name was forgotten, the user ca ask for a list of all the user names
- After log in a menu will show with the list of options:
  - Display Tasks 
  - Add Task 
  - Mark Task as Complete
  - Delete Task
  - Quit 
- Through this self explanatory simple menu, the user will be alble to manage all the tasks they need.

## Features 
------

### Welcome message and LogIn
- Here the user can enter the user name and the password

![Login](/assets/image/login.png)
- The app will then check with the spreadsheet where all the users and passwords are stored.

![Have a user name or forgot user name](assets/images/have_or_forgot_username.png)
- If user is new or forgot user name the app will ask.

![User List](assets/images/user_list.png)
- If "y" is chosen a list of all the users will be shown and then redirected to the login again.

![New user](assets/images/new_user.png)
- If "n" is chosen a the app will create a new user after asking for a password, that will get stored in the spreadsheet. and an acceptance message is shown.

### Multi Choice Menu
![Multi Choice Menu](assets/images/multi_choice_menu.png)
- After login a multi choice menu will appear

### Display Tasks
![Display Tasks](assets/images/display_tasks.png)
- A list with all the tasks is shown. If no tasks exist, a message "No tasks found." is shown.

### Add Task
![Add Task](assets/images/add_task.png)
- Here the user is offered the option adding new task to their list. When the task is added there is a confirmation message.

### Mark Task as Complete
![Mark Task as Complete](assets/images/mark_task_complete.png)
- A list of all the tasks is shown and the option to sellect which task to mark as complete is offered. When a task is selected there is a confirmation message that the task was marked as done.

### Delete Task 
![Delete Task](assets/images/delete_task.png)
- A list of all the tasks is shown and the option to sellect which task to delete is offered. When a task is selected there is a confirmation message that the tasks was deleted.

### Quit
![Quit](assets/images/delete_task.png)
- A thank you message and a goodbye greetting is displayed. The app is closed.

### Input Validation
- All inputs have input validators, which ask the user for either a string, or "y" or "n", or an integer (whole number). 
- Please see [Testing](/TESTING.md) page for more detailed explanation of this.

MAKE THE TABLE!!!!

### Potential Future Features

- Add option to make users work within the same worksheet throught the same tasks.
- Add due date options to the tasks.

## Testing
------
### CI PEP8 Python Linter
- I checked all of my Python code through the Code Institute Python Linter, which came back all clear.

![CI python linter pass](/assets/documentation/images.webp/python-linter-clear.webp)

------




