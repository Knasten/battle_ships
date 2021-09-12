import random

# Variables turns and num_ship declared here and later changed by user.
# Size declared for board size here so grid 5x5
# admitted_input is used to verify row and column input from user
turns = 32
num_ships = 7
size = 8
admitted_input = ['1', '2', '3', '4', '5']


# If player miss I will show an "-"
# If player hit I will show an "X"
# For water I will show "^"


def create_sea(board):
    """
    This function prints the board for the user to see.
    Aswell as printing out numbers for each row and column.
    """
    print('   1 2 3 4 5 6 7 8')
    print('  ----------------')
    row_number = 1
    for row in board:
        print("%d |%s|" % (row_number, "|".join(row)))
        row_number += 1


def create_ships(board, num_ships):
    """
    This function adds ship to a random place in the list which will then be
    printed by create_sea func.
    """
    for ships in range(num_ships):
        ship_row = random.randint(0, size - 1)
        ship_column = random.randint(0, size - 1)
        while board[ship_row][ship_column] == 'X':
            ship_row = random.randint(0, size - 1)
            ship_column = random.randint(0, size - 1)
        board[ship_row][ship_column] = 'X'


def get_ship_location():
    """
    This function asks the user to enter a row and column.
    If row and column returned from user is not valid it will print this,
    and ask for a new number til the user enters a valid.
    """
    row = input('Choose a row from 1 to 5: \n')
    while row not in admitted_input or row == "":
        print('Your number is not valid please try again!')
        row = input('Choose a row from 1 to 5: \n')
    column = input('Choose a column from 1 to 5: \n')
    while column not in admitted_input or column == "":
        print('Your number is not valid please try again!')
        column = input('Choose a column from 1 to 5: \n')
    return int(row) - 1, int(column) - 1


def count_hits(board):
    """
    This function looks for any ship that has been hit
    and then returns the value to our counter.
    """
    count = 0
    for row in board:
        for column in row:
            if column == 'X':
                count += 1
    return count

# unseen_board and guess_board will be the same size
# unseen_board used to verify hits and guess_board to show outcome.


unseen_board = [["^" for x in range(size)]for y in range(size)]
guess_board = [["^" for x in range(size)]for y in range(size)]


def main(turns, num_ships):
    """
    This function runs the game and prints out the result
    after each guess aswell as end result if turns go to
    zero or if count hit is the same as number of ships.
    """
    round = 0
    while turns > 0:
        print(f'Round {round}')
        create_sea(guess_board)
        row, column = get_ship_location()
        if guess_board[row][column] == 'X' or guess_board[row][column] == '-':
            print('You have already blown up theese coordinates!')
        elif unseen_board[row][column] == 'X':
            guess_board[row][column] = 'X'
            round += 1
            print('HIT! You sank a ship!')
            print(f'You have {turns} left before the enemy fleet sinks you!')
        else:
            print('MISS! Try again!')
            guess_board[row][column] = '-'
            round += 1
            turns -= 1
            print(f'You have {turns} turns left')
            print('Before the enemy fleet sinks you!')
        if count_hits(guess_board) == num_ships:
            print('You have WON!')
            print(f'It took you {round} rounds to sink {num_ships} ships')
            break
        elif turns == 0:
            print('Sorry. Your crew is sleeping with the fish!')
            break


def start_game():
    """
    This function starts the game!
    """
    print('Get ready! Set! Go! Battleships is starting!')
    create_ships(unseen_board, num_ships)
    main(turns, num_ships)


start_game()
