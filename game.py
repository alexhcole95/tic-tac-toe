def introduction():
    print("\nWelcome to Tic Tac Toe!")


def instructions():
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


def play():
    return input("\nAre you ready to play? Enter [Y] or [N]. ").upper().startswith('Y')


def choice():
    human_choice = ' '
    computer_choice = ' '
    while human_choice != 'X' or human_choice != 'O':

        human_choice = input(f"\n{human}, would you like to be X or O? ")[0].upper()

        if human_choice == 'X' or human_choice == 'O':
            break
        print("INVALID INPUT! Please Try Again!")

    if human_choice == 'X':
        computer_choice = 'O'
    elif human_choice == 'O':
        computer_choice = 'X'

    return human_choice, computer_choice


def first_player():
    import random
    return random.choice((0, 1))


def display_board(board):
    print("    " + " {} | {} | {} ".format(board[7], board[8], board[9]))
    print("    " + "-----------")
    print("    " + " {} | {} | {} ".format(board[4], board[5], board[6]))
    print("    " + "-----------")
    print("    " + " {} | {} | {} ".format(board[1], board[2], board[3]))


def player_choice(board, name, choice):
    position = 0

    while position not in [1, 2, 3, 4, 5, 6, 7, 8, 9] or not space_check(board, position):
        position = int(input(f'\n{name} ({choice}), Choose your next position: (1-9) '))

        if position not in [1, 2, 3, 4, 5, 6, 7, 8, 9] or not space_check(board, position) or position == "":

            print(f"INVALID INPUT. Please Try Again!\n")
    print("\n")
    return position
