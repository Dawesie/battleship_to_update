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


def position_ships(grid, size):
    """
    To determin the row and column positions of the battleships.
    """
    grid = board
    for x in range(size):
        y = randint(0, size - 1)
        board[x][y] = 'S'
    return grid


def get_guess(size, grid):
    """
    To get row and colum positon from the player, where torpedos
    are to be launched onto the board.
    """
    duplicate = True
    while duplicate is True:
        location = []
        row = input(f'Please enter a row number between 0 and {size - 1}.\n')
        row = validate_guess(row, size)
        location.append(row)
        col = input(f'Please enter a column value between 0 and {size - 1}.\n')
        col = validate_guess(col, size)
        location.append(col)
        duplicate = duplicate_check(location, grid)
    return location


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


def duplicate_check(check, grid):
    """
    To check for duplicate guesses and request new guess if there
    duplicate is given.
    """
    num1 = check[0]
    num2 = check[1]
    if grid[num1][num2] == 'X' or grid[num1][num2] == 'S':
        print(f'Current guess {check} is a duplicate\n')
        print('Please re-enter your guess.\n')
        duplicate = True
    else:
        duplicate = False
    return duplicate


def update_board(data, player, ships, sunk_ships):
    """
    Takes players guess, updates and prints the current playing board.
    """
    row = data[0]
    col = data[1]
    if ships[row][col] == 'S':
        print(f'Your {data} launch has resulted in a Hit!')
        print(f'Congratulations, Admiral {name}\n')
        player[row][col] = 'S'
        sunk_ships += 1
    else:
        print(f'Your {data} guess resulted in a miss.')
        player[row][col] = 'X'
    for r in player:
        for c in r:
            print(c, end=" ")
        print()
    return player, sunk_ships


name = input('Please enter your name: ')

print(f"Welcome to My Battleship Admiral {name}.\n")
print('Your mission:')
print("To locate and destroy all of the enemies' ")
print('battleships, BEFORE your torpedoes RUN OUT.\n')
print('*' * 50)
print('There are 4 missions to choose from,')
print('the higher the number, the greater the skill')
print('needed to complete your task.')
print('*' * 50)
print('Mission 0: Is a 3 x 3 grid, with 3 enemy ships,')
print('that must be destroyed with 6 torpeodoes.')
print()
print('Mission 1: Is a 4 x 4 grid, with 4 enemy ships,')
print('that must be destroyed with 11 torpeodoes.')
print()
print('Mission 2: Is a 5 x 5 grid, with 5 enemy ships,')
print('that must be destroyed with 17 torpeodoes.')
print('*' * 50)

max = 3
mission_level = input(f'Please select your mission number, Admiral {name} \n')
game = validate_guess(mission_level, max)
print(game)


board_size = 3
torpedos = 6
fleet = 3
player_board = [['o'] * board_size for x in range(board_size)]
board = create_board(board_size)
print()
print(f"player's guess: {player_board}")
ship_grid = position_ships(board, board_size)
print()
print(f'playing board with ships: {ship_grid}')
print()
battleships = 0
play_on = False
while play_on is False:
    guess = get_guess(board_size, player_board)
    result = update_board(guess, player_board, ship_grid, battleships)
    new_board = result[0]
    battleships = result[1]
    print()
    print(f'You have sunk {battleships} battleships.\n')
    torpedos -= 1
    print(f'You have {torpedos} torpedo(s) left.\n')
    if torpedos == 0 or battleships == fleet:
        print('!!! Mission Over !!!')
        play_on = True
        if torpedos == 0 or battleships != fleet:
            print('Enemy ships have evaded your tropedoes!')
            print(f'Better luck next time Admiral {name}!')
        else:
            if battleships == fleet:
                print(f'"Well done Admrial {name}')
                print('You have destroying the enemies fleet!')
    else:
        print('Launch another torpedo?')
        print('Press any key to continue or n to exit.')
        ans = input()
        print()
        if ans == 'n' or ans == 'N':
            play_on = True
            print(f"Mission has been aborted on Admiral {name}'s orders.")
