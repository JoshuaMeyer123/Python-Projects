# Greeting
print("Welcome to the tip calculator! ")

num_list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

# Storing user inputs in variables
x_bill = True
while x_bill:
    bill = input("What was the total bill? R")
    x_bill2 = True

    for i in bill:
        check = num_list.count(i)

        if check == 0:
            input("Only type numbers. Press enter to try again")
            x_bill2 = False
            break
    if x_bill2:
        x_bill = False

x_tip = True
while x_tip:
    tip = input("How much tip would you like to give? 10%, 12% or 15%? ")
    if len(tip)>2:
        input("Only type a two digit number without the '%' sign, press enter to try again.")
    else:
        x_tip = False

people = input("How many people to split the bill? ")

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
print(f"For a total payment: R{total_payment}")

