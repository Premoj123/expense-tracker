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
    print("\n--- All Expenses ---")
    if not expenses:
        print("No expenses recorded yet.")
        return
 
    print(f"{'ID':<5} {'Date':<12} {'Category':<15} {'Description':<25} {'Amount':>10}")
    print("-" * 70)
    for exp in expenses:
        print(f"{exp['id']:<5} {exp['date']:<12} {exp['category']:<15} {exp['description']:<25} Rs.{exp['amount']:>8.2f}")
    print("-" * 70)
    total = sum(e["amount"] for e in expenses)
    print(f"{'Total':<52} Rs.{total:>8.2f}")
 


#UPDATE THE EXPENSES
def update_expense(expenses):
    print("\n--- Update Expense ---")
    if not expenses:
        print("No expenses to update.")
        return
 
    view_expenses(expenses)
 
    try:
        exp_id = int(input("\nEnter ID to update: "))
    except ValueError:
        print("Invalid ID.")
        return
 
    expense = next((e for e in expenses if e["id"] == exp_id), None)
    if not expense:
        print("Expense not found.")
        return
 
    print(f"Editing: {expense['description']} | Rs.{expense['amount']} | {expense['category']}")
    print("Press Enter to keep current value.")
 
    new_desc = input(f"Description [{expense['description']}]: ").strip()
    if new_desc:
        expense["description"] = new_desc
 
    new_amount = input(f"Amount [{expense['amount']}]: ").strip()
    if new_amount:
        try:
            expense["amount"] = round(float(new_amount), 2)
        except ValueError:
            print("Invalid amount. Keeping old value.")
 
    categories = ["Food", "Transport", "Entertainment", "Shopping", "Bills", "Health", "Other"]
    print("Categories: " + ", ".join(f"{i+1}.{c}" for i, c in enumerate(categories)))
    new_cat = input(f"Category [{expense['category']}]: ").strip()
    if new_cat:
        try:
            expense["category"] = categories[int(new_cat) - 1]
        except (ValueError, IndexError):
            print("Invalid choice. Keeping old category.")
 
    save_expenses(expenses)
    print("Expense updated successfully.")
 


#DELETE THE EXPENSES
def delete_expense(expenses):
    print("\n--- Delete Expense ---")
    if not expenses:
        print("No expenses to delete.")
        return
 
    view_expenses(expenses)
 
    try:
        exp_id = int(input("\nEnter ID to delete: "))
    except ValueError:
        print("Invalid ID.")
        return
 
    expense = next((e for e in expenses if e["id"] == exp_id), None)
    if not expense:
        print("Expense not found.")
        return
 
    confirm = input(f"Delete '{expense['description']}' (Rs.{expense['amount']})? (y/n): ")
    if confirm.lower() == "y":
        expenses.remove(expense)
        for i, e in enumerate(expenses, 1):
            e["id"] = i
        save_expenses(expenses)
        print("Expense deleted successfully.")
    else:
        print("Deletion cancelled.")


#VIEW SUMMARY 
def view_summary(expenses):
    print("\n--- Expense Summary ---")
    if not expenses:
        print("No expenses recorded yet.")
        return
 
    total = sum(e["amount"] for e in expenses)
 
    category_totals = {}
    for e in expenses:
        category_totals[e["category"]] = category_totals.get(e["category"], 0) + e["amount"]
 
    print(f"\n{'Category':<20} {'Total':>10} {'%':>8}")
    print("-" * 42)
    for cat, amt in sorted(category_totals.items(), key=lambda x: x[1], reverse=True):
        percent = (amt / total) * 100
        print(f"{cat:<20} Rs.{amt:>7.2f} {percent:>7.1f}%")
    print("-" * 42)
    print(f"{'Total':<20} Rs.{total:>7.2f}")
 
    monthly_totals = {}
    for e in expenses:
        month = e["date"][:7]
        monthly_totals[month] = monthly_totals.get(month, 0) + e["amount"]
 
    if len(monthly_totals) > 1:
        print(f"\n{'Month':<15} {'Total':>10}")
        print("-" * 27)
        for month, amt in sorted(monthly_totals.items()):
            print(f"{month:<15} Rs.{amt:>7.2f}")
 
    highest = max(expenses, key=lambda e: e["amount"])
    print(f"\nHighest Expense : {highest['description']} - Rs.{highest['amount']:.2f} ({highest['category']})")
    print(f"Total Entries   : {len(expenses)}")
    print(f"Average         : Rs.{total / len(expenses):.2f}")
 


def main():
    expenses = load_expenses()
    while True:
        show_menu()
        choice = input("Enter your choice: ")
        handle_choice(choice, expenses)

if __name__ == "__main__":
    main()
