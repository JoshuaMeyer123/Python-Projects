from game_data import data
from art import logo, vs
import random
#from replit import clear

# def clear_console():
#     os.system('cls')


# Choose random dictionary from list
def choice():
    new_choice = random.choice(data)
    data.remove(new_choice)
    return new_choice


def compare(higher, lower):
    higher_followers = higher.get('follower_count')
    lower_followers = int(lower.get('follower_count'))
    if higher_followers > lower_followers:
        return 1
    elif higher_followers == lower_followers:
        return 1
    else:
        return 0


win = 1
score = 0
choice_B = 0
while win:
    #clear_console()
    # Introduction
    print(logo)
    if score > 0:
        print(f"You're right! Current score: {score}")
        choice_A = choice_B
    else:
        choice_A = choice()
    print(f"Compare A: {choice_A.get('name')}, a {choice_A.get('description')}, from {choice_A.get('country')}.")
    print(vs)
    choice_B = choice()
    print(f"Against B: {choice_B.get('name')}, a {choice_B.get('description')}, from {choice_B.get('country')}.")

    # Pose question
    question = input("Who has more followers? Type 'A' or 'B': ")
    if question == 'A':
        win = compare(choice_A, choice_B)
    else:
        win = compare(choice_B, choice_A)

    if win:
        score += 1
    else:
        print("Better luck next time")