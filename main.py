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


#ADD Expense 
def add_expense():
     pass

