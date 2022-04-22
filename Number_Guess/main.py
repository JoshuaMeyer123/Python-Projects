import random
from art import logo

# Function - setting difficulty and thus number of attempts
def level():
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if difficulty == 'hard':
        return 5
    elif difficulty == 'easy':
        return 10
    else:
        print("You did not type 'easy' or 'hard'.")
        return 0

# function - introduction and checking the guess
def game():

    # Introduction
    print(logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")

    # Choose a random number between 1 and 100
    chosen_number = random.randint(0, 100)

    attempts = level()

    # checks if guess matches the random number until attempts run out
    while attempts != 0:
      print(f"You have {attempts} attempts remaining to guess the number.")
      guess = int(input("Make a guess: "))
      if guess == chosen_number:
        attempts = 0
        win = 1
        print("You guessed the correct number!!!")
      else:
        attempts -= 1
        if guess < chosen_number:
          print("Too low")
        else:
          print("Too high")
        if attempts == 0:
            print("You have run out of attempts")

game()