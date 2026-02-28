print("---- Monthly Expense Calculator ----")

income = float(input("Enter your monthly income: "))

rent = float(input("Enter rent amount: "))
food = float(input("Enter food expense: "))
travel = float(input("Enter travel expense: "))
entertainment = float(input("Enter entertainment expense: "))
others = float(input("Enter other expenses: "))

total_expense = rent + food + travel + entertainment + others
savings = income - total_expense

print("\n------ Expense Summary ------")
print(f"Total Expense: ₹{total_expense}")
print(f"Savings: ₹{savings}")

if savings > 0:
    print("Good job! You saved money this month 💰")
elif savings == 0:
    print("You broke even this month.")
else:
    print("Warning! You spent more than you earned ⚠️")