# Creating a function that checks if the input contains non-digit characters
def num_check(thing):
    num_list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    bool1 = True
    while bool1:
        value = input(thing)
        bool2 = True
        for i in value:
            check = num_list.count(i)
            if check == 0:
                input("Only type numbers. Press enter to try again")
                bool2 = False
                break
        if bool2:
            bool1 = False
    return value

# Greeting
print("Welcome to the tip calculator! ")

# Storing user inputs in variables
bill = num_check("What was the total bill? R")

x_tip = True
while x_tip:
    tip = num_check("How much tip would you like to give? 10%, 12% or 15%? ")
    if len(tip)>2:
        input("Only type a two digit number without the '%' sign, press enter to try again.")
    else:
        x_tip = False

people = num_check("How many people to split the bill? ")

# Changing variable type to perform math operations
bill = float(bill)
tip = int(tip)
people = int(people)

# Calculating how much each person must pay and rounding the value to two decimal places
bill_and_tip = bill*(1+tip/100)
payment = round(bill_and_tip/people, 2)
total_payment = payment*people
total_payment = "{:.2f}".format(total_payment)
payment = "{:.2f}".format(payment)

# Final output
print(f"Each person should pay: R{payment}")
print(f"For a total payment of: R{total_payment}")

