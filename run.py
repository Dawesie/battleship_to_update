from random import randint


name = input(f'Hello!\n Please enter your name: ')


print(f"Welcome to My Battleship Admiral {name}.\n Your mission:\n To locate and destroy all of the enemies battleships \n before your torpedoes run out")


def create_board():
    """
    This function sets up a matrix from which the grid for the game will be used. 

    """
    matrix = "\n".join([" ".join(["0" for x in range(3)]) for y in range(3)])
    return matrix

def position_ships(row, col):
    """
    To determin the row and column positions of the battle ships. 
    """
    ship_row = row
    ship_col = col
    for x, y in zip(range(3),range(3)):
        x = randint(0,3)
        y = randint(0,3)
        ship_row.append(x)
        ship_col.append(y)
    return ship_row, ship_col

def duplicate_check(row, col):
    """
    Check to ensure there are no duplicate postions for the battleships or positon guessses. 
    """
    ship_row = row
    ship_col = col
    num = 0
    for x, y in zip(range(3),range(3)):
        if ship_row[num] and ship_col[num] = ship_row [num + 1] and ship_col[num + 1]:
           x = randint(0,3)
           ship_row.append[num] = x  




def get_gesses():
    pass

def validate_guess():
    pass


board = create_board()
print(board)
ship_row = []
ship_col =[]
position_ships(ship_row, ship_col)
print(ship_row, ship_col)

