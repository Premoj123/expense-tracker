import json 
import datetime 
#import os


#Loading From JSON
def load_expenses():
    try:  
        with open("expenses.json" , "r") as expense_file:
                return json.load(expense_file)
    except FileNotFoundError:
          return []
    

#Saving Into JSON
def save_expenses(expenses):
    with open("expenses.json" , "w") as expense_file:
         json.dump(expenses,expense_file,indent = 4)


#MENU
def show_menu():
    print("\n====== EXPENSE TRACKER ======")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Update Expense")
    print("4. Delete Expense")
    print("5. View Summary")
    print("6. Exit")



#Handling Choice
def handle_choice(choice,expenses):
    if choice == "1":
        add_expense(expenses)   

    elif choice == "2":
        view_expenses(expenses)

    elif choice == "3":
        update_expense(expenses)

    elif choice == "4":
        delete_expense(expenses)

    elif choice == "5":
        view_summary(expenses)

    elif choice == "6":
        save_expenses(expenses)
        print("Exiting Program....")
        return
    

    else:
        print("Invalid Choice.")


#ADD THE EXPENSES
def add_expense(expenses):
    pass


#VIEw THE EXPENSES
def view_expenses(expenses):
    pass


#UPDATE THE EXPENSES
def update_expense(expenses):
    pass


#DELETE THE EXPENSES
def delete_expense(expenses):
    pass


#VIEW SUMMARY 
def view_summary(expenses):
    pass


def main():
    expenses = load_expenses()
    while True:
        show_menu()
        choice = input("Enter your choice: ")
        handle_choice(choice, expenses)

if __name__ == "__main__":
    main()
