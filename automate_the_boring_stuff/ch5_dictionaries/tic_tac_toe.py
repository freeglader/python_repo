
#?###################################################################################################################################################################
#? Author: sullenbode
#? Program: Tic Tac Toe game
#? Description: use dictionaries to store X's and O's on the board. The board will be formatted with letters on the x-axis and numbers ascending from bottom to top on the y-axis.
#! Note - the game will not handle errors, keep track of score, or determine if you've won at this point. Might come back later to update it.
#?##################################################################################################################################################################

import random

# Create the board
theBoard = {'a1': ' ', 'a2': ' ', 'a3': ' ', 'b1': ' ', 'b2': ' ', 'b3': ' ', 'c1': ' ', 'c2': ' ', 'c3': ' '}

# Function that will print the board when called
def printBoard(board):
    print(board['a3'] + '|' + board['b3'] + '|' + board['c3'])
    print('-+-+-')
    print(board['a2'] + '|' + board['b2'] + '|' + board['c2'])
    print('-+-+-')
    print(board['a1'] + '|' + board['b1'] + '|' + board['c1'])

turn = input('X or O? ')
for i in range(9):
    printBoard(theBoard)
    choice = input('Place ' + turn + ' where on the board? ')
    theBoard[choice] = turn.upper()
    if turn.lower() == 'x':
        turn = 'O'
    else:
        turn = 'X'

 