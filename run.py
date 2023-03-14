from random import randint
import itertools


name = input(f'Hello!\n Please enter your name: ')
print(f'Your name is {name}')

print(f"Welcome to My Battleship Admiral {name}.\n Your mission:\n To locate and destroy all of the enemies battleships \n before your torpedoes run out")


def create_board():
    """
    This function sets up the grid and ransomly positons the battleships. 

    """
    grid = list(itertools.product(range(3), range(3)))
    print(grid)
    matrix = "\n".join([" ".join(["0" for x in range(3)]) for y in range(3)])
    print(matrix)

def set_board():
    pass

def get_gesses():
    pass

def validate_guess():
    pass


create_board()
