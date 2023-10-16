import gspread
import os
from google.oauth2.service_account import Credentials
from pprint import pprint

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

    if not first_task:
        print("\nNo tasks found.")
    else:
        print("\nTask List:\n")
        for i, row in enumerate(all_values[2:], start=1):  # Skip the header row
            name, status = row
            print(f"{i}. {name} ({status})")

def add_task(user):
    """
    Add a new task to the worksheet
    """
    name = input("Enter task name: ")
    status = "Not Done"
    data = [name, status]
    worksheet_to_update = SHEET.worksheet(user)
    worksheet_to_update.append_row(data)
    print(f"Task '{name}' added.")

def mark_complete(worksheet):
    """
    Mark a task as complete
    """
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
    display_tasks(worksheet)
    all_values = worksheet.get_all_values()
    choice = input("Enter the task number to delete: ")
    try:
        index = int(choice) - 1
        if 0 <= index < len(all_values):
            deleted_task = all_values.pop(index + 1)
            worksheet.clear()
            if all_values:
                worksheet.insert_rows(all_values)
            print(f"Task '{deleted_task[0]}' deleted.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Invalid input. Please enter a valid task number.")

def main():
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
            print("\nGoodbye!!!\n")
            break
        else:
            print("Invalid choice. Please choose a valid option.")

main()