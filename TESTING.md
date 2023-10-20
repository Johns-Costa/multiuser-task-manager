# Multi Task Manager

## Testing
------

Testing is carried out throughout the development of the project. This is often done before committing the changes to the repository, where the file is kept. Often, changes are done throughout the code writting that lead to errors and posterior fixing.

### Input Validation
Every input in the application needs to have input validation, to check the user input is the correct data type and within the range expected for the tasks being registered. Below is a table of the requirements that each input need for correct validation. All inputs will loop, often using a `while` loop with `try`, `except` and `else` statements following. If they do not use a `while` loop, an `if`/`elif`/`else` statement(s) is(/are) used in the code instead. 

| Function | data required | accepts | doen't accept | commets |
| --- | --- | --- | --- | --- |
| initial_input | strings | strings | Empty strings| - |
| check_user | strings | strings both for password and for user name | Empty strings/wrong user name/wrong password | creates new user name if new to the app |
| menu | up and down arrows and enter | only accepts ups and down arrows and enter buttons | does not accept anything else |  this menu helps navigation through the functions |
| display_tasks | none | nothing | nothing | displays the user tasks |
|  add_task | String | Any string | empty data | adds task |
|  mark_complete | Integer | Whole number | strings or numbers above the number os tasks | - |
|  edit_task | Integer and then string  | whole number and then string | first strings and then empty string | changes a task name |
|  delete_task | Integer | Whole number | strings or numbers above the number os tasks | deletes task |

Every input unaccepted input will send a specific error message explaing what was wrong. examples:
 - Invalid task number.
 - Invalid input. Please enter a valid task number.
 - Enter at least a single character to continue.




