#Expense Tracker Project

#List of all expenses
expenses = []; #List of expenses in form of dictionaries

print("Welcome to the expense tracker. Keep an eye on your expenses");

while True:
    print("===Menu===")
    print("1. Add Expense")
    print("2. View Expense")
    print("3. View total expense")
    print("4. Exit")

    choice = int(input("Enter your choice : "));

# 1. Add expense
    if (choice==1):
        date = input("Enter the date of expense : ");
        category = input("Enter the type of expense (eg. food, travel, shopping, etc.) : ");
        description = input("Details about the expense : ");
        amount = float(input("Enter the amount spent : "))

        expense = {
            "date": date,
            "category": category,
            "description": description,
            "amount": amount
        }

        expenses.append(expense);
        print(" \n Expense is added successfully.")

# 2. View Expenses

    elif (choice==2):
        if(len(expenses)==0):
            print("No expenses made. Go spend some money😅");
        else:
            print("These are all your expenses.")
            count = 1
            for eachExpense in expenses:
                print(f"Expense no. {count} -> {eachExpense["date"]}, {eachExpense["category"]}, {eachExpense["description"]}, {eachExpense["amount"]}")
                count+=1;

# 3. View Total Spending

    elif (choice==3):
        total = 0
        for eachExpense in expenses:
            total = total + eachExpense["amount"]

        print ("\n Total Expense : ", total);

# 4. Exit
    elif (choice==4):
        print ("Thank You! For using our system.")
        break

    else:
        print("Invalid Choice. Try Again");
