from numpy import full

# Create an array filled with blank strings
board = full((6, 7), " ")

# Variable exists to stop main loop when someone wins
win = False


def clear():
    # Clears the screen
    print("\n" * 100)


def displayBoard():
    # Prints the board
    print(" " + str(board)[1:-1])


def p1Input():
    selection = int(input("P1: Enter a row number between 1-7: "))

    # Makes it so the player has to actually put in an input
    done = False

    while not done:

        # Checks each row so the pieces can "stack" on each other
        if board[5][selection - 1] == " ":
            board[5][selection - 1] = "x"
            done = True

        elif board[4][selection - 1] == " ":
            board[4][selection - 1] = "x"
            done = True

        elif board[3][selection - 1] == " ":
            board[3][selection - 1] = "x"
            done = True

        elif board[2][selection - 1] == " ":
            board[2][selection - 1] = "x"
            done = True

        elif board[1][selection - 1] == " ":
            board[1][selection - 1] = "x"
            done = True

        elif board[0][selection - 1] == " ":
            board[0][selection - 1] = "x"
            done = True

        else:
            print("All spaces on this row are taken!")
            p1Input()
            done = True


def p2Input():
    selection = int(input("P2: Enter a row number between 1-7: "))

    # Makes it so the player has to actually put in an input
    done = False

    while not done:

        # Checks each row so the pieces can "stack" on each other
        if board[5][selection - 1] == " ":
            board[5][selection - 1] = "o"
            done = True

        elif board[4][selection - 1] == " ":
            board[4][selection - 1] = "o"
            done = True

        elif board[3][selection - 1] == " ":
            board[3][selection - 1] = "o"
            done = True

        elif board[2][selection - 1] == " ":
            board[2][selection - 1] = "o"
            done = True

        elif board[1][selection - 1] == " ":
            board[1][selection - 1] = "o"
            done = True

        elif board[0][selection - 1] == " ":
            board[0][selection - 1] = "o"
            done = True

        else:
            print("All spaces on this row are taken!")


def main():

    # Temp, might make a better way
    while not win:
        clear()
        displayBoard()
        p1Input()
        clear()
        displayBoard()
        p2Input()


main()
