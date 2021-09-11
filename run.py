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