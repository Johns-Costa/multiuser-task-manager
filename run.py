import os
import time
import gspread
from google.oauth2.service_account import Credentials
from simple_term_menu import TerminalMenu
from blessed import Terminal


SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('task-manager')

term = Terminal()


def display_tasks(worksheet):
    """
    Get all values from the  chosen worksheet
    """
    all_values = worksheet.get_all_values()
    first_task = worksheet.row_values(3)
    clear()
    if not first_task:
        print(term.black_on_yellow("\nNo tasks found."))
    else:
        print(term.cyan("\nTask List:\n"))
        for i, row in enumerate(all_values[2:], start=1):
            name, status = row
            print(term.cyan(f"{i}. {name} ({status})"))


def add_task(user):
    """
    Add a new task to the worksheet
    """
    print(term.black_on_darkkhaki
          (term.center
           ("Note: type 'exit' to go back to the menu")))
    name = input(term.cyan("\nEnter task name: "))
    if name == "exit":
        clear()
        menu(user)
    else:
        if name == '':
            print(term.red
                  ("Enter at least a single character to continue."))
            time.sleep(2)
            clear()
            add_task(user)
        else:
            status = "Not Done"
            data = [name, status]
            worksheet_to_update = SHEET.worksheet(user)
            worksheet_to_update.append_row(data)
            print(term.green(f"Task '{name}' added."))


def mark_complete(worksheet, user):
    """
    Mark a task as complete
    """
    clear()
    display_tasks(worksheet)
    all_values = worksheet.get_all_values()
    print(term.black_on_darkkhaki
          (term.center("Note: type 'exit' to go back to the menu")))
    choice = input(term.cyan
                   ("Enter the task number to mark as complete: "))
    if choice == "exit":
        clear()
        menu(user)
    else:
        try:
            index = int(choice)
            if 0 <= index < (len(all_values)-1):
                row = index + 2
                worksheet.update_cell(row, 2, 'Done')
                print(term.white_on_green
                      ("Task marked as complete."))
            else:
                print(term.red("Invalid task number."))
                time.sleep(2)
                mark_complete(worksheet, user)
        except ValueError:
            print(term.red
                  ("Invalid input. Please enter a valid task number."))
            time.sleep(2)
            mark_complete(worksheet, user)


def edit_task(worksheet, user):
    """
    Edits a task from the worksheet
    Marks the task as not done
    """
    clear()
    display_tasks(worksheet)
    all_values = worksheet.get_all_values()
    print(term.black_on_darkkhaki
          (term.center("Note: type 'exit' to go back to the menu")))
    choice = input(term.cyan
                   ("Enter the task number to edit:"))
    task = input(term.cyan
                 ("Enter the new task name: "))

    if choice == "exit":
        clear()
        menu(user)
    elif task == "exit":
        clear()
        menu(user)
    elif task == '':
        print(term.red
              ("Enter at least a single character to continue."))
        time.sleep(2)
        clear()
        edit_task(worksheet, user)
    else:
        try:
            index = int(choice)
            if 0 <= index < (len(all_values)-1):
                row = index + 2
                worksheet.update_cell(row, 1, task)
                worksheet.update_cell(row, 2, 'Not Done')
                print(term.white_on_green(f"Task edited as '{task}'."))
            else:
                print(term.red("Invalid task number."))
                time.sleep(2)
                edit_task(worksheet, user)
        except ValueError:
            print(term.red
                  ("Invalid input. Please enter a valid task number."))
            time.sleep(2)
            edit_task(worksheet, user)


def delete_task(worksheet, user):
    """
    Delete a task from the worksheet
    """
    clear()
    display_tasks(worksheet)
    all_values = worksheet.get_all_values()
    print(term.black_on_darkkhaki
          (term.center
           ("Note: type 'exit' to go back to the menu")))
    choice = input(term.cyan
                   ("Enter the task number to delete: "))
    if choice == "exit":
        clear()
        menu(user)
    else:
        try:
            index = int(choice) - 1
            if 0 <= index < (len(all_values)-2):
                deleted_task = all_values.pop(index + 2)
                worksheet.clear()
                if all_values:
                    worksheet.insert_rows(all_values)
                print(term.white_on_green
                      (f"Task '{deleted_task[0]}' deleted."))
            else:
                print(term.red("Invalid task number."))
                time.sleep(2)
                delete_task(worksheet, user)
        except ValueError:
            print(term.red
                  ("Invalid input. Please enter a valid task number."))
            time.sleep(2)
            delete_task(worksheet, user)


def initial_input():
    """
    Main menu for the Task Manager
    """

    while True:
        user = input(term.cyan
                     ("Please enter your name: "))

        if user != '':
            return user
        else:
            print(term.red
                  ('Enter at least a single character to continue.'))
            continue


def check_user(user):
    """
    Check if the user exists in the spreadsheet
    If not, create a new user
    Check if the password is correct
    If new user, create a password
    """
    try:
        worksheet = SHEET.worksheet(user)
        password = ()
        password_value = worksheet.acell('B1').value

        while password != password_value:
            password = input(term.cyan
                             ("Please enter your password: "))

            if password != password_value:
                print(term.black_on_red
                      ("Wrong password. Try again"))

            if password == password_value:
                print(term.black_on_green
                      ("Correct password!"))
                print("\n")
                break
    except:
        while True:
            forgot_user = input(
                term.black_on_cyan(
                 "Unknown user name.\n\nDo you have a user name?\
\n       or\nForgot your user name? (y/n): "))
            if forgot_user == "y":
                clear()
                print(term.cadetblue1("User name list:\n"))
                for num in range(len(SHEET.worksheets())):
                    all_users = SHEET.get_worksheet(num)
                    print(term.cadetblue1('* ', all_users.title))
                print("\n")
                print(term.black_on_darkkhaki(term.center
                                              ('press any key to continue.')))
                with term.cbreak(), term.hidden_cursor():
                    inp = term.inkey()
                if inp == term.KEY_ESCAPE:
                    continue

                main()
                break
            elif forgot_user == "n":
                print(term.cyan("Creating new user..."))
                SHEET.add_worksheet(user, 100, 100)
                worksheet = SHEET.worksheet(user)

                while True:
                    new_password = input(term.cyan
                                         ("Please enter a password: "))
                    if new_password != '':
                        print(term.green
                              ("Password accepted!\nNew user created!"))
                        worksheet.append_row(['Password:', new_password])
                        worksheet.append_row(['Task Name', 'Status'],)
                        worksheet.format('A2:B2',
                                         {'textFormat': {'bold': True}})
                        worksheet.freeze('2')
                        break
                    else:
                        print(term.red(
                         'Enter at least a single character to continue.'))
                        continue

                break
            else:
                print(term.black_on_red_bold
                      ("Invalid input. Please enter 'y' or 'n'."))


def menu(user):
    """
    Display the menu and call the appropriate function
    """
    while True:
        options = [" Display Tasks ",
                   " Add Task ", " Mark Task as Complete ",
                   " Edit Task ", " Delete Task ", " Quit "]
        terminal_menu = TerminalMenu(options,
                                     title=("\nEnter your choice:\n"),
                                     menu_cursor=(None),
                                     menu_highlight_style=("bg_cyan",
                                                           "fg_black"))
        menu_entry_index = terminal_menu.show()

        worksheet = SHEET.worksheet(user)
        if options[menu_entry_index] == " Display Tasks ":
            display_tasks(worksheet)
        elif options[menu_entry_index] == " Add Task ":
            add_task(user)
        elif options[menu_entry_index] == " Mark Task as Complete ":
            mark_complete(worksheet, user)
        elif options[menu_entry_index] == " Edit Task ":
            edit_task(worksheet, user)
        elif options[menu_entry_index] == " Delete Task ":
            delete_task(worksheet, user)
        elif options[menu_entry_index] == " Quit ":
            clear()
            print(term.black_on_cyan_bold
                  ("\nThank you for using the Task Manager!\n\nGoodbye!!!\n"))
            exit()
        else:
            print(term.red
                  ("Invalid choice. Please choose a valid option."))


def clear():
    """
    This clears the terminal to prevent clutter on it.
    """
    os.system('cls' if os.name == 'nt' else 'clear')


def main():
    """
    Run all program functions
    """
    print(term.black_on_cyan_bold
          ("\nWelcome to Task Manager!\n"))
    user = initial_input()
    check_user(user)
    menu(user)


if __name__ == "__main__":
    main()
