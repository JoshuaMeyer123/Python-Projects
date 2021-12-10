# Greeting
print("Welcome to the tip calculator! ")

# Storing user inputs in variables
bill = input("What was the total bill? R")
tip = input("How much tip would you like to give? 10, 12 or 15? ")
people = input("How many people to split the bill? ")

# Changing variable type to perform math operations
bill = float(bill)
tip = int(tip)
people = int(people)

# Calculations and rounding the value to two decimal places
bill_and_tip = bill*(1+tip/100)
payment = round(bill_and_tip/people, 2)
payment = "{:.2f}".format(payment)

# Final output
print(f"Each person should pay: R{payment}")
