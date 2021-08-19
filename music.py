def check_guess(guess, answer):
    global score
    still_guessing = True
    attempt = 0
    while still_guessing and attempt < 3:
        if guess.lower() == answer.lower():
            print("Correct!")
            score = score + 1
            still_guessing = False
        else:
            if attempt < 2:
                guess = input("That's not correct, try again! ")
            attempt = attempt + 1
    if attempt == 3:
        print("Correct answer is " + answer) 
score = 0
print("Welcome to a 90's music quiz ")
guess1 = input("Which band performed the song 'Romeo ja Julia?' ")
check_guess(guess1, "movetron")
guess2 = input("Who sang the song 'What is love'?")
check_guess = (guess2, "haddaway")
guess3 = input("What was Aqua's first hit? ")
check_guess = (guess3, "barbie girl")
guess4 = input("Who sang the song 'Trust me' ")
check_guess = (guess4, "pandora")
guess5 = input("Who was Ginger Spice?\n a) Geri\n b) Victoria\n c) Emma\n d) Mel C ")
check_guess = (guess5, 'a')


