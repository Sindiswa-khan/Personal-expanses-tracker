print("================================")
print("     PERSONAL EXPENSE TRACKER")
print("================================")

name = input("Enter your name: ")

income = float(input("Enter your monthly income (R): "))
food = float(input("Enter your food expenses (R): "))
transport = float(input("Enter your transport expenses (R): "))
other = float(input("Enter your other expenses (R): "))

total_expenses = food + transport + other
balance = income - total_expenses

print("\n========== SUMMARY ==========")
print(f"Name: {name}")
print(f"Monthly income: R{income:.2f}")
print(f"Total expenses: R{total_expenses:.2f}")
print(f"Money remaining: R{balance:.2f}")

if balance > 0:
    print("Good job! You have money left to save.")
elif balance == 0:
    print("You have spent all your income.")
else:
    print("Warning! Your expenses exceed your income.")

print("=============================")
