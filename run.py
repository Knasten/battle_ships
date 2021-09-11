import random

# If player miss I will show an "-"
# If player hit I will show an "X"
# For water I will show "^"


def create_sea(board):
    print('   1 2 3 4 5')
    print('  -----------')
    row_number = 1
    for row in board:
        print("%d |%s|" % (row_number, "|".join(row))
        row_number += 1


def get_ship_location():
    row = input('Choose a row from 1 to 5')
    while row not in "12345":
        print('Your number is not valid please try again!')
        row = input('Choose a row from 1 to 5')
    column = input('Choose a column from 1 to 5')
    while column not in "12345":
        print('Your number is not valid please try again!')
        column = input('Choose a column from 1 to 5')