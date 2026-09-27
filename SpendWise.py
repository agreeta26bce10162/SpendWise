expenses = []
income = []
budget = 0


# ADD INCOME
def add_income():

    amount = float(input("Enter income amount: "))

    if amount <= 0:
        print("Amount must be greater than 0.")
        return

    category = input("Enter income category: ")
    description = input("Enter description: ")
    date = input("Enter month and year (MM/YYYY): ")
    payment_method = input("Enter payment method: ")

    transaction_id = len(income) + len(expenses) + 1

    income.append([
        transaction_id,
        amount,
        category,
        description,
        date,
        payment_method
    ])

    print("\nIncome added successfully!")


# ADD EXPENSE
def add_expense():

    amount = float(input("Enter expense amount: "))

    if amount <= 0:
        print("Amount must be greater than 0.")
        return

    category = input("Enter expense category: ")
    description = input("Enter description: ")
    date = input("Enter month and year (MM/YYYY): ")
    payment_method = input("Enter payment method: ")

    transaction_id = len(income) + len(expenses) + 1

    expenses.append([
        transaction_id,
        amount,
        category,
        description,
        date,
        payment_method
    ])

    print("\nExpense added successfully!")


# VIEW TRANSACTIONS
def view_transactions():

    print("\n===== TRANSACTIONS =====")

    if len(expenses) == 0 and len(income) == 0:

        print("No transactions found.")

    else:

        print("\n--- INCOME ---")

        if len(income) == 0:

            print("No income recorded.")

        else:

            for i in range(len(income)):

                item = income[i]

                print("\nIncome ID:", item[0])
                print("Amount:", item[1])
                print("Category:", item[2])
                print("Description:", item[3])
                print("Month/Year:", item[4])
                print("Payment Method:", item[5])

        print("\n--- EXPENSES ---")

        if len(expenses) == 0:

            print("No expenses recorded.")

        else:

            for i in range(len(expenses)):

                item = expenses[i]

                print("\nExpense ID:", item[0])
                print("Amount:", item[1])
                print("Category:", item[2])
                print("Description:", item[3])
                print("Month/Year:", item[4])
                print("Payment Method:", item[5])


# MANAGE BUDGET
def manage_budget():

    print("\n===== BUDGET MANAGEMENT =====")

    budget = float(input("Enter monthly budget: "))

    if budget <= 0:

        print("Budget must be greater than 0.")
        return

    total_expenses = 0

    for item in expenses:

        total_expenses = total_expenses + item[1]

    remaining = budget - total_expenses
    percentage = (total_expenses / budget) * 100

    print("\nTotal Budget: ₹", budget)
    print("Total Expenses: ₹", total_expenses)
    print("Remaining Budget: ₹", remaining)
    print("Budget Used:", percentage, "%")

    if percentage >= 100:

        print("Status: Budget Exceeded!")
        print("Warning: You have exceeded your budget!")

    elif percentage >= 90:

        print("Status: Budget Almost Used!")
        print("Warning: You have used 90% or more of your budget!")

    elif percentage >= 75:

        print("Status: Budget Usage is High.")

    else:

        print("Status: Budget is under control.")


# SPENDING ANALYSIS
def spending_analysis():

    print("\n===== SPENDING ANALYSIS =====")

    categories = []

    for item in expenses:

        category = item[2]

        if category not in categories:

            categories.append(category)

    if len(categories) == 0:

        print("No expenses recorded.")

    else:

        total_expenses = 0

        for item in expenses:

            total_expenses = total_expenses + item[1]

        for category in categories:

            total = 0

            for item in expenses:

                if item[2] == category:

                    total = total + item[1]

            percentage = (total / total_expenses) * 100

            print(category + ":", total, "(", percentage, "%)")

        print("\nTotal Expenses:", total_expenses)


# SAVINGS
def view_savings():

    total_income = 0
    total_expenses = 0

    for item in income:

        total_income = total_income + item[1]

    for item in expenses:

        total_expenses = total_expenses + item[1]

    savings = total_income - total_expenses

    print("\n===== SAVINGS =====")
    print("Total Income:", total_income)
    print("Total Expenses:", total_expenses)
    print("Savings:", savings)

    if total_income > 0:

        savings_percentage = (savings / total_income) * 100

        print("Savings Percentage:", savings_percentage, "%")

    else:

        print("Savings Percentage: 0 %")


# MONTHLY REPORT
def monthly_report():

    month = input("Enter month and year for report (MM/YYYY): ")

    total_income = 0
    total_expenses = 0

    for item in income:

        if item[4] == month:

            total_income = total_income + item[1]

    for item in expenses:

        if item[4] == month:

            total_expenses = total_expenses + item[1]

    savings = total_income - total_expenses

    print("\n===== MONTHLY REPORT =====")
    print("Month:", month)
    print("Total Income:", total_income)
    print("Total Expenses:", total_expenses)
    print("Savings:", savings)

    if total_income > 0:

        savings_percentage = (savings / total_income) * 100

        print("Savings Percentage:", savings_percentage, "%")

    else:

        print("Savings Percentage: 0 %")

    print("\n--- CATEGORY-WISE EXPENSES ---")

    categories = []

    for item in expenses:

        if item[4] == month:

            category = item[2]

            if category not in categories:

                categories.append(category)

    if len(categories) == 0:

        print("No expenses recorded for this month.")

    else:

        for category in categories:

            total = 0

            for item in expenses:

                if item[4] == month and item[2] == category:

                    total = total + item[1]

            percentage = (total / total_expenses) * 100

            print(category + ":", total, "(", percentage, "%)")


# EDIT TRANSACTION
def edit_transaction():

    print("\n===== EDIT TRANSACTION =====")

    print("1. Edit Income")
    print("2. Edit Expense")

    edit_type = input("Enter your choice: ")

    if edit_type == "1":

        if len(income) == 0:

            print("No income available.")

        else:

            for i in range(len(income)):

                print(
                    income[i][0],
                    ".",
                    income[i][1],
                    income[i][2],
                    income[i][3]
                )

            number = int(input("Enter income ID to edit: "))

            found = False

            for i in range(len(income)):

                if income[i][0] == number:

                    amount = float(input("Enter new amount: "))
                    category = input("Enter new category: ")
                    description = input("Enter new description: ")
                    date = input("Enter month and year (MM/YYYY): ")
                    payment_method = input("Enter new payment method: ")

                    income[i] = [
                        number,
                        amount,
                        category,
                        description,
                        date,
                        payment_method
                    ]

                    print("Income updated successfully!")

                    found = True

            if found == False:

                print("Invalid transaction ID.")

    elif edit_type == "2":

        if len(expenses) == 0:

            print("No expenses available.")

        else:

            for i in range(len(expenses)):

                print(
                    expenses[i][0],
                    ".",
                    expenses[i][1],
                    expenses[i][2],
                    expenses[i][3]
                )

            number = int(input("Enter expense ID to edit: "))

            found = False

            for i in range(len(expenses)):

                if expenses[i][0] == number:

                    amount = float(input("Enter new amount: "))
                    category = input("Enter new category: ")
                    description = input("Enter new description: ")
                    date = input("Enter month and year (MM/YYYY): ")
                    payment_method = input("Enter new payment method: ")

                    expenses[i] = [
                        number,
                        amount,
                        category,
                        description,
                        date,
                        payment_method
                    ]

                    print("Expense updated successfully!")

                    found = True

            if found == False:

                print("Invalid transaction ID.")

    else:

        print("Invalid choice.")


# DELETE TRANSACTION
def delete_transaction():

    print("\n===== DELETE TRANSACTION =====")

    print("1. Delete Income")
    print("2. Delete Expense")

    delete_type = input("Enter your choice: ")

    if delete_type == "1":

        if len(income) == 0:

            print("No income available.")

        else:

            for i in range(len(income)):

                print(
                    income[i][0],
                    ".",
                    income[i][1],
                    income[i][2]
                )

            number = int(input("Enter income ID to delete: "))

            found = False

            for i in range(len(income)):

                if income[i][0] == number:

                    income.pop(i)

                    print("Income deleted successfully!")

                    found = True

                    break

            if found == False:

                print("Invalid transaction ID.")

    elif delete_type == "2":

        if len(expenses) == 0:

            print("No expenses available.")

        else:

            for i in range(len(expenses)):

                print(
                    expenses[i][0],
                    ".",
                    expenses[i][1],
                    expenses[i][2]
                )

            number = int(input("Enter expense ID to delete: "))

            found = False

            for i in range(len(expenses)):

                if expenses[i][0] == number:

                    expenses.pop(i)

                    print("Expense deleted successfully!")

                    found = True

                    break

            if found == False:

                print("Invalid transaction ID.")

    else:

        print("Invalid choice.")


# SEARCH TRANSACTION
def search_transaction():

    print("\n===== SEARCH TRANSACTION =====")

    search = input("Enter category or description to search: ").lower()

    found = False

    print("\n--- INCOME ---")

    for item in income:

        if search in item[2].lower() or search in item[3].lower():

            print("Income ID:", item[0])
            print("Amount:", item[1])
            print("Category:", item[2])
            print("Description:", item[3])
            print("Month/Year:", item[4])
            print("Payment Method:", item[5])
            print()

            found = True

    print("\n--- EXPENSES ---")

    for item in expenses:

        if search in item[2].lower() or search in item[3].lower():

            print("Expense ID:", item[0])
            print("Amount:", item[1])
            print("Category:", item[2])
            print("Description:", item[3])
            print("Month/Year:", item[4])
            print("Payment Method:", item[5])
            print()

            found = True

    if found == False:

        print("No matching transaction found.")


# MAIN PROGRAM

while True:

    print("\n========== SPENDWISE ==========")

    print("1. Add Income")
    print("2. Add Expense")
    print("3. View Transactions")
    print("4. Manage Budget")
    print("5. View Spending Analysis")
    print("6. View Savings")
    print("7. Generate Monthly Report")
    print("8. Edit Transaction")
    print("9. Delete Transaction")
    print("10. Search Transaction")
    print("11. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":

        add_income()

    elif choice == "2":

        add_expense()

    elif choice == "3":

        view_transactions()

    elif choice == "4":

        manage_budget()

    elif choice == "5":

        spending_analysis()

    elif choice == "6":

        view_savings()

    elif choice == "7":

        monthly_report()

    elif choice == "8":

        edit_transaction()

    elif choice == "9":

        delete_transaction()

    elif choice == "10":

        search_transaction()

    elif choice == "11":

        print("Thank you for using SpendWise!")
        break

    else:

        print("Invalid choice! Please enter a number from 1 to 11.")
