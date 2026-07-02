def add_expense():
    name = input("Enter expense name: ")
    category = input("Enter category: ")
    amount = input("Enter amount: ")
    date = input("Enter date (DD-MM-YYYY): ")

    with open("expenses.txt", "a") as file:
        file.write(f"{name},{category},{amount},{date}\n")

    print("Expense Added Successfully!\n")


def view_expenses():
    try:
        with open("expenses.txt", "r") as file:
            print("\n------ Expenses ------")
            for line in file:
                name, category, amount, date = line.strip().split(",")
                print(name, "|", category, "| ₹", amount, "|", date)
            print()
    except FileNotFoundError:
        print("No expenses found.\n")


def total_expense():
    total = 0
    try:
        with open("expenses.txt", "r") as file:
            for line in file:
                name, category, amount, date = line.strip().split(",")
                total += float(amount)

        print("Total Expense = ₹", total, "\n")

    except FileNotFoundError:
        print("No expenses found.\n")


def search_expense():
    category = input("Enter category to search: ")

    try:
        with open("expenses.txt", "r") as file:
            found = False

            for line in file:
                name, cat, amount, date = line.strip().split(",")

                if cat.lower() == category.lower():
                    print(name, "|", cat, "| ₹", amount, "|", date)
                    found = True

            if not found:
                print("No expense found.")

    except FileNotFoundError:
        print("No expenses found.")


def delete_expense():
    try:
        with open("expenses.txt", "r") as file:
            expenses = file.readlines()

        for i, expense in enumerate(expenses):
            print(i + 1, expense.strip())

        choice = int(input("Enter expense number to delete: "))

        expenses.pop(choice - 1)

        with open("expenses.txt", "w") as file:
            file.writelines(expenses)

        print("Expense Deleted Successfully!\n")

    except FileNotFoundError:
        print("No expenses found.")

    except:
        print("Invalid Choice.")


def edit_expense():
    try:
        with open("expenses.txt", "r") as file:
            expenses = file.readlines()

        for i, expense in enumerate(expenses):
            print(i + 1, expense.strip())

        choice = int(input("Enter expense number to edit: "))

        name = input("Enter new name: ")
        category = input("Enter new category: ")
        amount = input("Enter new amount: ")
        date = input("Enter new date: ")

        expenses[choice - 1] = f"{name},{category},{amount},{date}\n"

        with open("expenses.txt", "w") as file:
            file.writelines(expenses)

        print("Expense Updated Successfully!\n")

    except FileNotFoundError:
        print("No expenses found.")

    except:
        print("Invalid Choice.")


while True:
    print("===== Expense Tracker =====")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Total Expense")
    print("4. Search Expense")
    print("5. Delete Expense")
    print("6. Edit Expense")
    print("7. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_expense()

    elif choice == "2":
        view_expenses()

    elif choice == "3":
        total_expense()

    elif choice == "4":
        search_expense()

    elif choice == "5":
        delete_expense()

    elif choice == "6":
        edit_expense()

    elif choice == "7":
        print("Thank You!")
        break

    else:
        print("Invalid Choice.\n")
