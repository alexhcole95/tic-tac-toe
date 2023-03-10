import random


def instructions():
    # This function shows the instructions to the game.
    print("\nAfter selecting [PLAY] you will choose to be either 'X' or 'O'.\n")
    print("Once your selection has been made, the program will randomly select which player goes first.\n")
    print("The example below shows the layout of the board; it matches the numpad keys on a keyboard.\n")
    print(" 7 | 8 | 9 ")
    print("-----------")
    print(" 4 | 5 | 6 ")
    print("-----------")
    print(" 1 | 2 | 3 ")
    print("\nYou only have to select a position from 1-9.\n")
    print("Good Luck!")


def mark():
    # This is a function that allows P1 to pick X or O. P2 will receive the unselected choice.
    p1_mark = ' '
    p2_mark = ' '
    while p1_mark != 'X' or p1_mark != 'O':
        p1_mark = input(f"\n{player_1}, would you like to be X or O? ")[0].upper()

        if p1_mark == 'X' or p1_mark == 'O':
            break
        print("INVALID INPUT! Please Try Again!")

    if p1_mark == 'X':
        p2_mark = 'O'
    elif p1_mark == 'O':
        p2_mark = 'X'

    return p1_mark, p2_mark


def first_player():
    # This function determines if P1 or P2 goes first.
    return random.choice((0, 1))


def play():
    # This function verifies if the user is ready to play.
    return input("\nAre you ready to play? Enter [Y] or [N]. ").upper().startswith('Y')


def display_board(board):
    # This function is the tic-tac-toe board with the {}s formatted to numbers 1-9.
    print("    " + " {} | {} | {} ".format(board[7], board[8], board[9]))
    print("    " + "-----------")
    print("    " + " {} | {} | {} ".format(board[4], board[5], board[6]))
    print("    " + "-----------")
    print("    " + " {} | {} | {} ".format(board[1], board[2], board[3]))


def place_mark(board, choice, pos):
    # This function replaces the whitespace at the position on the board.
    board[pos] = choice


def space_check(board, pos):
    # This function checks whether the given position is empty or occupied.
    return board[pos] == ' '


def player_choice(board, name, choice):
    # This is the choice function that allows P1 and P2 to choose their position on the board.
    pos = 0

    while pos not in [1, 2, 3, 4, 5, 6, 7, 8, 9] or not space_check(board, pos):
        pos = int(input(f'\n{name} ({choice}), Choose your next position: (1-9) '))

        if pos not in [1, 2, 3, 4, 5, 6, 7, 8, 9] or not space_check(board, pos) or pos == "":

            print(f"INVALID INPUT. Please Try Again!\n")
    print("\n")
    return pos


def full_board_check(board):
    # This function checks if the board is full, meaning the game is a draw.
    for i in range(1, 10):
        if space_check(board, i):
            return False
    return True


def win_check(board, choice):
    # This function checks if there is a pattern of three Xs or Os.

    return (
            # Horizontal patterns:
            (board[1] == choice and board[2] == choice and board[3] == choice)
            or (board[4] == choice and board[5] == choice and board[6] == choice)
            or (board[7] == choice and board[8] == choice and board[9] == choice)
            # Vertical patterns:
            or (board[1] == choice and board[4] == choice and board[7] == choice)
            or (board[2] == choice and board[5] == choice and board[8] == choice)
            or (board[3] == choice and board[6] == choice and board[9] == choice)
            # Diagonal patterns:
            or (board[1] == choice and board[5] == choice and board[9] == choice)
            or (board[3] == choice and board[5] == choice and board[7] == choice))


def replay():
    # This function asks the user if they'd like to play again.
    return input('\nPlay Again? [Y] or [N]: ').lower().startswith('y')


# START OF PROGRAM
print("\nWelcome to Tic Tac Toe!")

while True:
    # This is an empty board.
    theBoard = [' '] * 10

    # This lists the options to the user.
    print("\nInstructions - [0]")
    print("\nPlay - [1]")

    # The following code executes differently depending on the option selected.
    option = (input("\nSelect option [0] or [1]:\t"))
    if option == str(0):
        instructions()
        continue

    elif option == str(1):
        # Asks for names of P1 and P2.
        player_1 = input("\nWhat is the name of Player One? ")
        player_2 = input("\nWhat is the name of Player Two? ")

        # Asks P1 for preferred choice and prints the assigned marks of the players.
        play1_choice, play2_choice = mark()
        print(f"\n{player_1}:", play1_choice)
        print(f"{player_2}:", play2_choice)

    else:
        print("\nINVALID INPUT! Please Try Again!")
        continue

    # This is the random function that determines and prints if P1 or P2 goes first.
    if first_player():
        turn = player_2
    else:
        turn = player_1
    print(f"\n{turn} will go first!")

    # This function asks if the user is ready to play.
    play_game = play()
    while play_game:
        # The following executes only if it's P1's turn:
        if turn == player_1:

            # Formats the empty board.
            display_board(theBoard)

            # Assigns the player's choice to position.
            position = player_choice(theBoard, player_1, play1_choice)
            print(f'\n{player_1} ({play1_choice}) has placed on {position}\n')

            # Places the mark on the board from position.
            place_mark(theBoard, play1_choice, position)

            # Checks if the mark causes a win:
            if win_check(theBoard, play1_choice):
                display_board(theBoard)
                print(f'\n\n{player_1}! Excellent work, YOU WON!\n\n')
                play_game = False

            # Checks if the mark causes a draw:
            else:
                if full_board_check(theBoard):
                    display_board(theBoard)
                    print('\nThis game is a draw!\n')
                    break

            # If the mark isn't a win or draw, it changes the turn to P2.
                else:
                    turn = player_2

        # The following executes only if it's P2's turn:
        elif turn == player_2:

            # Formats the empty board.
            display_board(theBoard)

            # Assigns the player's choice to position.
            position = player_choice(theBoard, player_2, play2_choice)
            print(f'\n{player_2} ({play2_choice}) has placed on {position}\n')

            # Places the mark on the board from position.
            place_mark(theBoard, play2_choice, position)

            # Checks if the mark causes a win:
            if win_check(theBoard, play2_choice):
                display_board(theBoard)
                print(f'\n\n{player_2}! Excellent work, YOU WON!\n\n')
                play_game = False

            # Checks if the mark causes a draw:
            else:
                if full_board_check(theBoard):
                    display_board(theBoard)
                    print('\nThis game is a draw!\n')
                    break

                # If the mark isn't a win or draw, it changes the turn to P1.
                else:
                    turn = player_1

    # Once the game is over, it asks if the user wants to play again.
    if replay():
        continue
    else:
        break

print("\nTHANKS FOR PLAYING!")
