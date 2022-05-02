# Import section


# Menu
menu = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
            "milk": 0,
        },
        "cost": 25,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 37,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 40,
        },
        "cost": 3.0,
    }
}


resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0.0,
}


# TODO: 1. Prompt user to choose what coffee they want
def coffee_choice():
    """Ask user what type of coffee they would like"""
    coffee = input("What would you like? (espresso/latte/cappuccino):")
    return coffee


# TODO: 2. Print report
def report():
    """Give a status report on the resources in the coffee machine"""
    print(f"Water: {resources.get('water')}ml")
    print(f"Milk: {resources.get('milk')}ml")
    print(f"Coffee: {resources.get('coffee')}g")
    print("Money: ${:0.2f}".format(resources.get('money')))


# TODO: 3. Check if resources are sufficient
def resource_check(coffee_request):
    """Check if there are sufficient resources to make the chosen coffee"""
    items = ['water', 'milk', 'coffee']
    for item in items:
        if resources.get(item) < (menu[coffee_request])['ingredients'].get(item):
            print(f"Sorry there is not enough {item}.")
            return 0
        else:
            return 1


# TODO: 4. Process coins
def process_coins():
    """Allows the user to submit there money. User can only use coins"""
    print("Please insert coins.")
    five = int(input("How many R5 coins?:"))
    two = int(input("How many R2 coins?:"))
    one = int(input("How many R1 coins?:"))
    fifty = int(input("How many 50c coins?:"))
    total = five*5 + two*2 + one*1 + fifty*0.50
    return total


# TODO: 5. Check if transaction is successful
def transaction(coffee_request):
    """Check if user has provided enough money to purchase chosen coffee"""
    total = process_coins()
    change = total - (menu[coffee_request]).get('cost')
    if change >= 0:
        print("Here is R{:0.2f} in change.".format(change))
    else:
        print("Sorry that is not enough money. Money refunded.")


# TODO: 6. Make Coffee
def brew_coffee(coffee_request):
    """Update the resources in the coffee machine"""
    new_water = resources.get('water') - (menu[coffee_request])['ingredients'].get('water')
    new_milk = resources.get('milk') - (menu[coffee_request])['ingredients'].get('milk')
    new_coffee = resources.get('coffee') - (menu[coffee_request])['ingredients'].get('coffee')
    new_money = resources.get('money') + menu[coffee_request].get('cost')
    resources['water'] = new_water
    resources['milk'] = new_milk
    resources['coffee'] = new_coffee
    resources['money'] = new_money
    print(f"Here is your {coffee_request} :) Enjoy!")


# TODO: 7. Compile everything to run as desired
more_coffee = True
while more_coffee:
    coffee_type = coffee_choice()
    if coffee_type == 'report':
        report()
    elif coffee_type == 'off':
        more_coffee = False
    elif coffee_type == 'espresso' or 'latte' or 'cappuccino':
        if resource_check(coffee_type):
            transaction(coffee_type)
            brew_coffee(coffee_type)
    else:
        print("You have not entered a valid input, try again.")

