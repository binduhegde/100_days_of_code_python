'''Welcome to the tip calculator!
What was the total bill? $100
How much tip would you like to give? 10, 12, or 15? 30
How many people to split the bill?3
Each person should pay: $43.33'''

print("Welcome to the tip calculator!")
bill = int(input("What was the total bill? $"))
tip = int(input("How much tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill? "))
print(f"Each person should pay: ${(bill + (bill*tip)/100)/people:.2f}")