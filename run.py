from random import randint


name = input(f'Hello!\n Please enter your name: ')


print(f"Welcome to My Battleship Admiral {name}.\n Your mission:\n To locate and destroy all of the enemies battleships \n before your torpedoes run out")


def create_board():
    """
    This function sets up a matrix from which the grid for the game will be used. 

    """
    matrix = "\n".join([" ".join(["0" for x in range(3)]) for y in range(3)])
    return matrix

def position_ships():
    ship = []
    for x, y in zip(range(3),range(3)):
        x = randint(0,3)
        y = randint(0,3)
        coord = (x,y)
        ship.append(coord)
    print(ship)

def get_gesses():
    pass

def validate_guess():
    pass


board = create_board()
print(board)
position_ships()

