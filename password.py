import random
import string

adjectives = ['great', 'malicious', 'benevolent', 'dreamy', 'itchy', 'beautiful', 'horrible', 
'sleepy', 'tired', 'pink', 'purple', 'fluffy', 'silent', 'courageous', 'juicy']

nouns = ['dragon', 'dinosaur', 'coffecup', 'television', 'banana', 'watermelon', 'hammer', 'plumber', 
'airconditioning', 'headrest']

colors = ['blue', 'yellow', 'purple', 'red', 'bloodred', 'orange', 'pink', 'green']

print('Welcome to choose your password! ')

while True: 
    for num in range(3):
        adjective = random.choice(adjectives)
        noun = random.choice(nouns)
        number = random.randrange(0,100)
        color = random.choice(colors)
        special_char = random.choice(string.punctuation)

        password = adjective + noun + color + str(number) + special_char
        print('Your new passord is ' + password)

    response = input('Do you want another password? Answer yes or no: ')
    if response == 'no':
        break

