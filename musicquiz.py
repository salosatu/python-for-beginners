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
guess1 = input('Who sang the song What is love')
check_guess(guess1, 'haddaway')
guess2 = input('Which band performed the hit song "Romeo ja Julia"?')
check_guess(guess2, 'movetron')
guess3 = input('What was the first hit of the Danish band Aqua? ')
check_guess(guess3, 'barbie girl')
print('Your score is ' + str(score))