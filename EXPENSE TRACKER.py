expensesList = []  # list of expense in form of dictionary
print("Welcome to Expense Tracker")

while True:
    print("====MENU====")
    print("1. Add Expense")
    print("2. View All Expenses")
    print("3. View Total Expense")
    print("4. Exit")

    choice = int(input("Please Enter Your Choice: "))  # Convert input to integer

    # 1. ADD EXPENSE
    if choice == 1:
        date = input("Enter the date: ")
        category = input("Enter category (food, makeup, book, travel...): ")
        description = input("Enter more details: ")
        amount = float(input("Enter the amount: "))

        expense = {
            "date": date,
            "category": category,
            "description": description,
            "amount": amount
        }

        expensesList.append(expense)
        print("\nExpenses added Successfully!")

    # 2. VIEW ALL EXPENSES
    elif choice == 2:
        if len(expensesList) == 0:
            print("No Expenses Added.")
        else:
            print("==== Your Total Expenses ====")
            count = 1
            for eachExpense in expensesList:
                print(f"Expense Number {count} -> {eachExpense['date']}, {eachExpense['category']}, {eachExpense['description']}, {eachExpense['amount']}")
                count += 1

    # 3. View Total Spending
    elif choice == 3:
        total = 0
        for eachExpense in expensesList:
            total += eachExpense["amount"]

        print("\nTotal Expense = ", total)

    # 4. Exit
    elif choice == 4:
        print("Thank You for using Expense Tracker <3 ")
        break

    else:
        print("Invalid Choice. Try again!")
