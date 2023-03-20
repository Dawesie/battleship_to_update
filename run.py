from random import randint
from array import *

name = input(f'Hello!\nPlease enter your name: ')


print(f"Welcome to My Battleship Admiral {name}.\n")
print(f'Your mission:')
print(f"To locate and destroy all of the enemies' battleships,") 
print(f'BEFORE your torpedoes RUN OUT.\n')


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


def position_ships(board, size):
    """
    To determin the row and column positions of the battleships. 
    To place the battleships on the board.
    """
    for x in range(size):
        y = randint(0,size - 1)
        board[x][y] = 'S'
    return board


def get_guess(size):
    """
    To get row and colum positon from the player, where torppedos
    are to be launched onto the board. 
    """
    guess = []
    row = input(f'Please enter a row number between 0 and {size - 1}\n')
    row = validate_guess(row, size)
    guess.append(row)
    print(f'Row value is: {row}')
    col = input(f'Please enter a column value between 0 and {size - 1}\n')
    col = validate_guess(col, size)
    guess.append(col)
    print(f'Column value is: {col}')
    return guess

def validate_guess(num, size):
    """
    To check the values entered are intergers, that
    values do not exceed the size of the board.
    """
    ok = False
    while ok == False:
        try:
            num == int(num)
            if  not int(num) >= 0:
                raise ValueError
            elif not int(num) <= size-1:
                raise ValueError
            else:
                ok = True
        except ValueError:
            print(f'Your input must be a whole number between 0 and {size-1}.')
            num = input(f'Please type in a number:\n')
    print(num)
    return int(num)
  
 

grid_size = 3
player_guess = [['o'] * grid_size for x in range(grid_size)] 
board = create_board(grid_size)
print() 
print(f"player's guess: {player_guess}")
print(f'playing board: {board}')
ship_grid = position_ships(board, grid_size)
print()
print(f'playing board with ships: {ship_grid}')
print()
guess = get_guess(grid_size)
print()
print(guess)

