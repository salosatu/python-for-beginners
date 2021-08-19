def check_guess(guess, answer):
    global score
    still_guessing = True
    attempt = 0
    while still_guessing and attempt < 3:
        if guess.lower() == answer.lower():
            print('The answer is correct!')
            score = score + 1
            still_guessing = False
        else:
            if attempt < 2:
                guess = input("That's incorrect, please try again. ")
            attempt = attempt + 1
    if attempt == 3:
        print('The correct answer is ' + answer)
score = 0
print('Guess the animal ')
guess1 = input('Which bear lives at the North Pole? ')
check_guess(guess1, 'polar bear')
guess2 = input('Which animal is the king of the jungle? ')
check_guess(guess2, 'lion')
guess3 = input('Which animal can learn to speak? ')
check_guess(guess3, 'parrot')
print('Your score is ' + str(score))