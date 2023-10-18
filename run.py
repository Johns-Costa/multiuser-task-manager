import gspread
import os
from google.oauth2.service_account import Credentials
from pprint import pprint
import keyboard

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('task-manager')

def display_tasks(worksheet):
    """ 
    Get all values from the  chosen worksheet
    """
    all_values = worksheet.get_all_values()
    first_task = worksheet.row_values(3)
    clear() 
    if not first_task:
        print("\nNo tasks found.")
    else:
        print("\nTask List:\n")
        for i, row in enumerate(all_values[2:], start=1):
            name, status = row
            print(f"{i}. {name} ({status})")
    

def add_task(user):
    """
    Add a new task to the worksheet
    """
    name = input("Enter task name: \n(Type 'exit' to go back to the menu.)")
    if "exit":
        menu(user)
        clear()
    else:
        status = "Not Done"
        data = [name, status]
        worksheet_to_update = SHEET.worksheet(user)
        worksheet_to_update.append_row(data)
        print(f"Task '{name}' added.")

def mark_complete(worksheet):
    """
    Mark a task as complete
    """
    clear() 
    display_tasks(worksheet)
    all_values = worksheet.get_all_values()
    choice = input("Enter the task number to mark as complete: ")
    try:
        index = int(choice) - 1
        if 0 <= index < len(all_values):
            row = index + 3
            worksheet.update_cell(row, 2, 'Done')
            print("Task marked as complete.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Invalid input. Please enter a valid task number.")

def delete_task(worksheet):
    """
    Delete a task from the worksheet
    """
    clear() 
    display_tasks(worksheet)
    all_values = worksheet.get_all_values()
    choice = input("Enter the task number to delete: ")
    try:
        index = int(choice) - 1
        if 0 <= index < len(all_values):
            deleted_task = all_values.pop(index + 2)
            worksheet.clear()
            if all_values:
                worksheet.insert_rows(all_values)
            print(f"Task '{deleted_task[0]}' deleted.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Invalid input. Please enter a valid task number.")

def initial_input():
    """
    Main menu for the Task Manager
    """

    while True:
        user = input("Please enter your name: ")

        if user != '':
            return user

            
        else:
            print('Enter at least a single character to continue.')
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
            password = input("Please enter your password: ")

            if password != password_value: 
                print("Wrong password. Try again") 
                
            if password == password_value:
                print("Correct password!")
                break    
            
    except:
        while True:
            forgot_user = input("Unknown user name.\n\nDo you have a user name?\n       or\nForgot your user name? (y/n): ")
            if forgot_user == "y":
                clear()
                print("User name list:\n")
                for num in range(len(SHEET.worksheets())):
                    all_users = SHEET.get_worksheet(num)  
                    pprint(all_users.title)
                input("Press Enter to go back to the main menu.")
                main()
                break       
            elif forgot_user == "n":
                print("User not found")
                print("Creating new user...")
                SHEET.add_worksheet(user, 100, 100)
                worksheet = SHEET.worksheet(user)
                
                while True:
                    new_password = input("Please enter a password: ")
                    if new_password != '':
                        print("Password accepted!\nNew user created!") 
                        worksheet.append_row(['Password:', new_password])
                        worksheet.append_row(['Task Name', 'Status'],)
                        worksheet.format('A2:B2', {'textFormat': {'bold': True}})
                        worksheet.freeze('2')
                        break
                        
                    else:
                        print('Enter at least a single character to continue.')
                        continue

                break
            else:
                print("Invalid input. Please enter 'y' or 'n'.")


def menu(user):
    """
    Display the menu and call the appropriate function
    """
    while True:
        print("\nTask Manager Menu:")
        print("\n1. Display Tasks")
        print("2. Add Task")
        print("3. Mark Task as Complete")
        print("4. Delete Task")
        print("5. Quit")

        choice = input("\n   Enter your choice: ")
        worksheet = SHEET.worksheet(user)
        if choice == "1":
            display_tasks(worksheet)
        elif choice == "2":
            add_task(user)
        elif choice == "3":
            mark_complete(worksheet)
        elif choice == "4":
            delete_task(worksheet)
        elif choice == "5":
            clear()
            print("\nThank you for using the Task Manager!\n\nGoodbye!!!\n")
            exit()
        else:
            print("Invalid choice. Please choose a valid option.")

def clear():
    """
    This clears the terminal to prevent clutter on it.
    """
    os.system('cls' if os.name=='nt' else 'clear')
    

def main():
    """
    Run all program functions
    """

    print("\nWelcome to Task Manager!\n")
    user = initial_input()
    check_user(user)
    menu(user)
   
   
main()