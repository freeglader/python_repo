
#TODO: The number guessing game will look something like the following:
#TODO: I am thinking of a number between 1 and 20. Take a guess. (Guess is too low, guess is too high)

#? My implementation, done before checking solution in the book:

import random

print('Let\'s play a game. I will pick a number between 1 and 20, and you will get 5 guesses. Ready?')
response = input()

def newGame():
        
    if response.lower() == 'yes':
        answer = random.randint(1,20)
        count = 1
        while count <= 5:
            guess = int(input('Guess number ' + str(count) + ': '))
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
    elif response.lower() == 'no':
        print('Okay :( bye!')
    else:
        print('Please answer either yes or no.') #? Couldn't figure out how to make this loop back to the start of the if statement correctly
        
newGame()

#* The book's implementation:

import random

secretNumber = random.randint(1,20)
print('I\'m thinking of a number between 1 and 20.')

#* Allow 6 guesses
for guessesTaken in range(1,7): #* This makes the program loop through 6 times, and stops the loop when guessesTaken reaches 6.
    print('Take a guess!\n')
    guess = int(input())
    
    if guess < secretNumber:
        print('Sorry, your guess was too low.')
    elif guess > secretNumber:
        print('Sorry, your guess was too high.')
    else:
        break #* If the guess ends up being the correct answer, it breaks out of the loop & sends execution to the next line
if guess == secretNumber: #! You have to put this in an if loop, because there is also another way the loop could stop: running out of tries.
    print('You got it! You got it in ' + str(guessesTaken) + ' tries!')
else:
    print('Sorry, you ran out of tries. The number was ' + str(secretNumber))
