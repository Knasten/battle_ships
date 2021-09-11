import random


turns = 10
num_ships = 4
size = 5


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
        print("%d |%s|" % (row_number, "|".join(row)))
        row_number += 1


def create_ships(board, num_ships, size):
    """
    This function adds ship to a random place in the list which will then be
    printed by create_sea func.
    """
    for ships in range(num_ships):
        ship_row = random.randint(0, size)
        ship_column = random.randint(0, size)
        while board[ship_row][ship_column] == 'X':
            ship_row = random.randint(0, size)
            ship_column = random.randint(0, size)
        board[ship_row][ship_column] = 'X'


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


unseen_board = [["^" for x in range(5)]for y in range(5)]
guess_board = [["^" for x in range(5)]for y in range(5)]
create_ships(unseen_board, num_ships, size)


def main(turns):
    """
    This function runs the game and prints out the result
    after each guess aswell as end result if turns go to
    zero or if count hit is the same as number of ships.
    """
    while turns > 0:
        print('Get ready! Set! Go! Battleships is starting!')
        create_sea(guess_board)
        row, column = get_ship_location()
        if guess_board[row][column] == 'X' or guess_board[row][column] == '-':
            print('You have already blown up theese coordinates!')
        elif unseen_board[row][column] == 'X':
            print('HIT! You sank a ship!')
        else:
            print('MISS! Try again!')
            guess_board[row][column] = '-'
            turns -= 1
            print(f'You have {turns} left before the enemy fleet sinks you!')
        if count_hits(guess_board) == num_ships:
            print('You have WON! GG!')
    print('Sorry. Your crew is sleeping with fish!')


main(turns)
