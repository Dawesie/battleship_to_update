from random import randint
from array import *

name = input(f'Hello!\n Please enter your name: ')


print(f"Welcome to My Battleship Admiral {name}.\n Your mission:\n To locate and destroy all of the enemies battleships \n before your torpedoes run out")


def create_board(data):
    """
    This function sets up a grid on which the game will be palyed.

    """
    grid_size = data
    grid = [['o']*grid_size for x in range(grid_size)] 
    for r in grid:
        for c in r:
            print(c,end = " ")
        print()
    return grid



def position_ships(board):
    """
    To determin the row and column positions of the battle ships. 
    """
    ship_board = board
    for x in range(3):
        y = randint(0,2)
        ship_board[x][y] = 'S'
    return ship_board




def get_gesses():
    pass

def validate_guess():
    pass


grid_size = 3
board = create_board(grid_size)
print(board)
ship_grid = position_ships(board)
print(ship_grid)

