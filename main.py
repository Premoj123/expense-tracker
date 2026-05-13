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
    print("\n--- Add Expense ---")
    description = input("Description: ").strip()
    if not description:
        print("Description cannot be empty.")
        return
 
    try:
        amount = float(input("Amount (Rs.): "))
        if amount <= 0:
            print("Amount must be greater than zero.")
            return
    except ValueError:
        print("Invalid amount. Please enter a number.")
        return
 
    categories = ["Food", "Transport", "Entertainment", "Shopping", "Bills", "Health", "Other"]
    print("Categories:")
    for i, cat in enumerate(categories, 1):
        print(f"  {i}. {cat}")
    cat_choice = input("Choose category (1-7): ").strip()
 
    try:
        category = categories[int(cat_choice) - 1]
    except (ValueError, IndexError):
        category = "Other"
 
    expense = {
        "id": len(expenses) + 1,
        "description": description,
        "amount": round(amount, 2),
        "category": category,
        "date": datetime.date.today().strftime("%Y-%m-%d")
    }
 
    expenses.append(expense)
    save_expenses(expenses)
    print(f"Expense '{description}' of Rs.{amount:.2f} added successfully.")
 


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
