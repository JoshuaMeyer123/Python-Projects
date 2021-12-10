# import modules
import random

# symbols for the three options
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''


options_symbol = [rock, paper, scissors]
options_names = ["rock", "paper", "scissors"]

x = True

while x:
    choice = input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n")

    if choice == "0" or choice == "1" or choice == "2":
        choice_int = int(choice)
        print(f"You chose: {options_names[choice_int]}")
        print(options_symbol[choice_int])

        computer_choice = random.randint(0, 2)
        print(f"Computer chose: {options_names[computer_choice]}")
        print(options_symbol[computer_choice])

        if choice_int == 0 and computer_choice == 2:
            print("You win")
        elif choice_int == 0 and computer_choice == 1:
            print("You loose")
        elif choice_int == 1 and computer_choice == 0:
            print("You win")
        elif choice_int == 1 and computer_choice == 2:
            print("You loose")
        elif choice_int == 2 and computer_choice == 1:
            print("You win")
        elif choice_int == 2 and computer_choice == 0:
            print("You loose")
        else:
            print("Draw")

        x = False
    else:
        print('You have not entered "0", "1" or "2". Try again.')
