import random
import art
import words

chosen_word = random.choice(words.word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6
used_letters = []
# Display game logo
print(art.logo)

# Testing code
print(f'Pssst, the solution is {chosen_word}.')

# Create empty list
display = []
for _ in range(word_length):
    display += "_"

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    # Check if user repeats a correctly guessed letter
    if guess in display:
        print(f"You have already guessed the letter {guess}")

    else:
        # Check guessed letter
        for position in range(word_length):
            letter = chosen_word[position]

            if letter == guess:
                display[position] = letter

        # Check if user is wrong.
        if guess not in chosen_word:
            # Let user know their guess is incorrect and subtract a life
            print(f"The letter {guess} is not in the word")
            lives -= 1

            # Check if user has run out of lives and if so end game
            if lives == 0:
                end_of_game = True
                print("!!! You lose !!!")

        # Join all the elements in the list and turn it into a String.
        print(f"{' '.join(display)}")

        # Check if user has got all letters.
        if "_" not in display:
            end_of_game = True
            print("!!! You win !!!")

        # Show hangman art progression
        print(art.stages[lives])

