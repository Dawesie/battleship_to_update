from random import randint
from array import *

name = input(f'Hello!\n Please enter your name: ')


print(f"Welcome to My Battleship Admiral {name}.\n Your mission:\n To locate and destroy all of the enemies battleships \n before your torpedoes run out")


def create_board(data):
    """
    This function sets up a grid on which the game will be palyed.

    """
    grid = [['o'] * data for x in range(data)] 
    for r in grid:
        for c in r:
            print(c,end = " ")
        print()
    return grid


def position_ships(board):
    """
    To determin the row and column positions of the battle ships. 
    """
    for x in range(3):
        y = randint(0,2)
        board[x][y] = 'S'
    return board


def get_guess(size):
    """
    To get row and colum positon from the player, where torppedos are to be launched. 
    """
    guess = []
    row = input(f'Please enter a row value between 0 and {size - 1}\n')
    print (f'You entered {row}')
    validate_guess(row)


def validate_guess(value):

    print(value)


grid_size = 3
board = create_board(grid_size)
print(board)
ship_grid = position_ships(board)
print(ship_grid)
guess = get_guess(grid_size)

