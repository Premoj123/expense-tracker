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


