import random


# If player miss I will show an "-"
# If player hit I will show an "X"
# For water I will show "^"


def create_sea(board):
    """
    This function prints the board for the user to see.
    Aswell as printing out numbers for each row and column.
    """
    print('   1 2 3 4 5')
    print('  -----------')
    row_number = 1
    for row in board:
        print("%d |%s|" % (row_number, "|".join(row))
        row_number += 1


"""
This function adds ship to a random place in the list which will then be
printed by create_sea func.
"""
def create_ships(board):
    for ships in range(num_ships):
        boat_row = random.randint(0, size)
        boat_column = random.randint(0, size)
        while board[boat_row][boat_column] == 'X'
            boat_row = random.randint(0, size)
            boat_column = random.randint(0, size)
        board[boat_row][boat_column] = 'X'


def get_ship_location():
    """
    This function asks the user to enter a row and column.
    If row and column returned from user is not valid it will print this,
    and ask for a new number til the user enters a valid.
    """
    row = input('Choose a row from 1 to 5')
    while row not in "12345":
        print('Your number is not valid please try again!')
        row = input('Choose a row from 1 to 5')
    column = input('Choose a column from 1 to 5')
    while column not in "12345":
        print('Your number is not valid please try again!')
        column = input('Choose a column from 1 to 5')


def count_hits(board):
    """
    This function looks for any ship that has been hit
    and then returns the value to our counter.
    """
    count = 0
    for row in board:
        for column in row:
            if board[row][column] == 'X':
                count += 1
    return count
