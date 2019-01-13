
#TODO: The number guessing game will look something like the following:
#TODO: I am thinking of a number between 1 and 20. Take a guess. (Guess is too low, guess is too high)

import random

print('Let\'s play a game. I will pick a number between 1 and 20, and you will get 5 guesses. Ready?')
response = input()

def newGame():
    if response.lower() == 'yes':
        answer = random.randint(1,20)
        count = 1
        while count <= 5:
            guess = int(input('Guess number ' + str(count)))
            count += 1
            if guess == answer:
                print('Wow, you won! Great job! The answer was ' + str(answer))
                break
            elif guess < answer:
                print('Too low! Try again.')
                continue
            elif guess > answer:
                print('Too high! Try again.')
                continue
        if count >= 5:
            print('Sorry, out of guesses! The answer was ' + str(answer))
        else:
            print('Thanks for playing!')

newGame()


