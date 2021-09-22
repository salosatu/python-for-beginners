import random
from words import words
import string


def get_word(words):
    word = random.choice(words)
    return word.upper()


def hangman():
    word = get_word(words)
    word_letters = set(word)  # letters in the word
    alphabet = set(string.ascii_uppercase)
    used_letters = set()  # what has been guessed

    lives = 8

    # getting user input
    while len(word_letters) > 0 and lives > 0:
        # letters used
        print(f"You have {lives} lives left and you have used the letters: ", ' '.join(
            used_letters))

        # current word
        word_list = [
            letter if letter in used_letters else '-' for letter in word]
        print("Current word: ", ' '.join(word_list))

        user_letter = input("Guess a letter: ").upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)

            else:
                lives -= 1
                print("Letter is not in this word.")

        elif user_letter in used_letters:
            print("You have already used that character, give it another go!")

        else:
            print("Invalid character, try again!")

    if lives == 0:
        print(f"Game over. The word was {word}")
    else:
        print(f"You guessed the word {word}")


hangman()
