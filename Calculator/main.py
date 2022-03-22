from art import logo
# creating the functions for the operations

# add
def add(n1, n2):
    return n1 + n2

# subtract
def subtract(n1, n2):
    return n1 - n2

# multiply
def multiply(n1, n2):
    return n1 * n2

# divide
def divide(n1, n2):
    return n1 / n2

# creating a dictionary
operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

#
def calculate():
    num1 = float(input("What's the first number? "))
    x = True
    while x:
        for operation in operations:
            print(operation)
        chosen_operation = (input("Pick an operation: "))
        num2 = float(input("What's the next number? "))
        answer = operations[chosen_operation](num1, num2)
        print(f"{num1} {chosen_operation} {num2} = {answer}")
        num1 = answer
        continue_calc = input(f"Type 'y' to continue calculating with {answer}, type 'n' to start new calculation, or type 'e' to exit: ")
        if continue_calc == 'y':
            x = True
        elif continue_calc == 'n':
            x = False
            calculate()
        else:
            x = False

print(logo)
calculate()