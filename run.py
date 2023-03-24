from random import randint


def create_board(data):
    """
   To set up the grid on which the game will be palyed.
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
    """
    grid = board
    for x in range(size):
        y = randint(0, size - 1)
        board[x][y] = 'S'
    return grid


def get_guess(size, board):
    """
    To get row and colum positon from the player, where torpedos
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
    values do not exceed the size of the board.
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


def duplicate_check(num, grid):
    pass


def update_board(data, board, ships):
    """
    Takes players guess, updates and prints the current playing board.
    """
    row = data[0]
    col = data[1]
    if ships[row][col] == 'S':
        print(f'Your {data} guess resulted in a Hit!')
        board[row][col] = 'S'
        print(board)
    else:
        print(f'Your {data} guess resulted in a miss.')
        board[row][col] = 'X'
        print(board)
    for r in board:
        for c in r:
            print(c, end=" ")
        print()
    return board


name = input('Hello!\nPlease enter your name: ')


print(f"Welcome to My Battleship Admiral {name}.\n")
print('Your mission:')
print("To locate and destroy all of the enemies' ")
print('battleships, BEFORE your torpedoes RUN OUT.\n')
print('*' * 50)
print()
print('There are 4 missions to choose from,')
print('the higher the number, the greater the sKill')
print('needed to complete your task.')


board_size = 3
torpedos = 2
player_board = [['o'] * board_size for x in range(board_size)]
board = create_board(board_size)
print()
print(f"player's guess: {player_board}")
ship_grid = position_ships(board, board_size)
print()
print(f'playing board with ships: {ship_grid}')
print()
play_on = False
while play_on == False and torpedos > 0:
    guess = get_guess(board_size, player_board)
    print()
    new_board = update_board(guess, player_board, ship_grid)
    print()
    torpedos -= 1
    print(f'You have {torpedos} torpedo(s) left')
    print('Launch another torpedo?')
    print('Press any key to contiue or n to exit.')
    ans = input()
    print(ans)
    if ans == 'n' or ans == 'N':
        play_on = True
        print('Game has stopped at your request')
print(torpedos)
