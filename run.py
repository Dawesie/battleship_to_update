from random import randint
from array import *

name = input('Hello!\nPlease enter your name: ')


print(f"Welcome to My Battleship Admiral {name}.\n")
print('Your mission:')
print("To locate and destroy all of the enemies' battleships,")
print('BEFORE your torpedoes RUN OUT.\n')


def create_board(data):
    """
    This function sets up a grid on which the game will be palyed.
    """
    grid = [['o'] * data for x in range(data)]
    for r in grid:
        for c in r:
            print(c, end=" ")
        print()
    return grid


def position_ships(board, size):
    """
    To determin the row and column positions of the battleships.
    To place the battleships on the board.
    """
    for x in range(size):
        y = randint(0, size - 1)
        board[x][y] = 'S'
    return board


def get_guess(size, grid):
    """
    To get row and colum positon from the player, where torppedos
    are to be launched onto the board. 
    """
    guess = []
    row = input(f'Please enter a row number between 0 and {size - 1}.\n')
    row = validate_guess(row, size)
    guess.append(row)
    print(f'Row value is: {row}')
    col = input(f'Please enter a column value between 0 and {size - 1}.\n')
    col = validate_guess(col, size)
    guess.append(col)
    print(f'Column value is: {col}')
    print()
    return guess


def validate_guess(num, size):
    """
    To check the values entered are intergers, that
    values do not exceed the size of the board and
    there are no duplicate guesses.
    """
    ok = False
    while ok is False:
        try:
            num = int(num)
            if int(num) < 0 or int(num) > size-1:
                raise ValueError
            else:
                ok = True
        except ValueError:
            print(f'Your input must be a whole number between 0 and {size-1}.')
            num = input('Please type in a number:\n')
    return int(num)


def update_board(data, board, ships):
    if ships[data[0]][data[1]] == 'S':
        print(f'Your {data} guess resulted in a Hit')
        board[data[0]][data[1]] = 'S'
        print(board)
    else:
        print(f'Your {data} guess resulted in a miss')
        board[data[0]][data[1]] = 'X'
        print(board)
    
    for r in board:
        for c in r:
            print(c, end=" ")
        print()
    return board


board_size = 3
player_board = [['o'] * board_size for x in range(board_size)] 
board = create_board(board_size)
print()
print(f"player's guess: {player_board}")
ship_grid = position_ships(board, board_size)
print()
print(f'playing board with ships: {ship_grid}')
print()
guess = get_guess(board_size, player_board)
print()
print(guess)
new_board = update_board(guess, player_board, ship_grid)
print(new_board)


