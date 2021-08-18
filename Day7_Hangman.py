#Step 4
import random
import hangman_art
import hangman_words
# from replit import clear
# import clear
print(hangman_art.logo)
stages = hangman_art.stages
end_of_game = False
word_list = hangman_words.word_list
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

#TODO-1: - Create a variable called 'lives' to keep track of the number of lives left.
#Set 'lives' to equal 6.

#Testing code
# print(f'Pssst, the solution is {chosen_word}.')

#Create blanks
print("")
print(f"The word is {word_length} letters long")
print("")

display = []
i = len(stages)-1
val = True
for _ in range(word_length):
    display += "_"

while not end_of_game and i > 0:
    guess = input("Guess a letter: ").lower()
    # clear()
    #Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        # print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
        if letter == guess:
            val = True
            display[position] = letter

    if guess not in chosen_word:
        i -= 1
        print(stages[i])
    else:
        print(stages[i])

    if i != 0:
        print(f"{' '.join(display)}")
        print(" ")

    #Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You Win.")
    elif i == 0:
        print(f"""You Lost because the word was '{chosen_word}'""")


    #TODO-3: - print the ASCII art from 'stages' that corresponds to the current number of 'lives' the user has remaining.