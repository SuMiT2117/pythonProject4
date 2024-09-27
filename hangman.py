import random

# Stages of the hangman game
stages = [
    ''' _______
     |/      |
     |      (_)
     |      \|/
     |       |
     |      / \\
     |
 ___|___''',

    ''' _______
     |/      |
     |      (_)
     |      \|/
     |       |
     |      / 
     |
 ___|___''',

    ''' _______
     |/      |
     |      (_)
     |      \|/
     |       |
     |      
     |
 ___|___''',

    ''' _______
     |/      |
     |      (_)
     |      \|/
     |       
     |      
     |
 ___|___''',

    ''' _______
     |/      |
     |      (_)
     |      \|
     |       
     |      
     |
 ___|___''',

    ''' _______
     |/      |
     |      (_)
     |       |
     |       
     |      
     |
 ___|___''',
]

# Word list
word_list = ["cheetah", "elephant", "lion", "tiger"]

lives = 6
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

# Create a placeholder to track progress
placeholder = ["_"] * word_length
print(" ".join(placeholder))

game_over = False
correct_letters = []

while not game_over:
    guess = input("Guess a letter: ").lower()

    # Check if the guessed letter is in the word
    if guess in chosen_word:
        for position in range(word_length):
            if chosen_word[position] == guess:
                placeholder[position] = guess
        print("Good guess!")
    else:
        lives -= 1
        print(f"Wrong guess! Lives left: {lives}")
        print(stages[lives])

    # Display the updated placeholder
    print(" ".join(placeholder))

    # Check if the player has won
    if "_" not in placeholder:
        game_over = True
        print("You win!")

    # Check if the player has lost
    if lives == 0:
        game_over = True
        print(f"You lose! The word was '{chosen_word}'.")
