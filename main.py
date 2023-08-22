import random
import hangman_words
import hangman_art

word_list = hangman_words.word_list
end_of_game = False
chosen_word = random.choice(word_list)
word_length = len(chosen_word)
lives = 6

print(hangman_art.logo)
#for test purposes
print(f'the solution is {chosen_word}.')

display = []
for _ in chosen_word:
    display += "_"
print(display)
while not end_of_game:

    guess = input("Guess a Letter: ").lower()

    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
    if guess not in chosen_word:
        lives -= 1
        print(f"Wrong letter. You have {lives} left")
    if lives == 0:
        end_of_game = False
        print("You lost")

    #Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

    if "_" not in display:
        end_of_game = True
        print("You win")

    print(hangman_art.stages[lives])