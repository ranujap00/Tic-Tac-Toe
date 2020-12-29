# designing a board

cell = ["-", "-", "-",
        "-", "-", "-",
        "-", "-", "-"]


def display_board():
    print("|" + cell[0] + "|" + cell[1] + "|" + cell[2] + "|")
    print("|" + cell[3] + "|" + cell[4] + "|" + cell[5] + "|")
    print("|" + cell[6] + "|" + cell[7] + "|" + cell[8] + "|")


def check_strike():
    # check horizontally
    for i in range(0, len(cell), 3):
        if cell[i] == cell[i+1] == cell[i+2] == "o" or cell[i] == cell[i+1] == cell[i+2] == "x":
            return True

    # check vertically
    for i in range(0, 3):
        if cell[i] == cell[i+3] == cell[i+6] == "o" or cell[i] == cell[i+3] == cell[i+6] == "x":
            return True

    # check diagonally
    if cell[0] == cell[4] == cell[8] == "o" or cell[0] == cell[4] == cell[8] == "x":
        return True
    elif cell[2] == cell[4] == cell[6] == "o" or cell[2] == cell[4] == cell[6] == "x":
        return True
    else:
        return False


def check_win(player):
    win = check_strike()
    if win:
        print(f"{player} won the game")
        play_again()


def check_all_occupied():
    for e in cell:
        if e == "-":
            return False


def is_tie():
    tie = check_all_occupied()
    if tie != False:
        print("it is a TIE!!!!")
        play_again()


def play_again():
    play = input("do you wan't to play again?: (y/n) ").lower()
    while not play.isalpha():
        play = input("do you wan't to play again?: (y/n) ").lower()

    if play == 'y':
        play_game()
    elif play == 'n':
        print("OK, Thanks for playing")
        exit(0)
    else:
        print("enter y or n")


def refresh():
    for c in range(len(cell) - 1):
        cell[c] = "-"


def play_game():
    refresh()

    print("WELCOME TO TIC TAC TOE")
    print()
    print()

    player1 = input("name of 1st player (o is assigned): ")
    player2 = input("name of 2nd player (x is assigned): ")

    display_board()
    print("As in the board, 1 represents the first cell and 9 represents the last cell")

    while True:
        while True:
            is_tie()

            value1 = input(f"{player1}, enter the position: ")
            while (not value1.isdigit()) or int(value1) > 9 or int(value1) <= 0:
                print("enter a numeric value between 1 and 9")
                value1 = input(f"{player1}, enter the position: ")

            value1 = int(value1)
            if cell[value1 - 1] == "-":
                cell[value1 - 1] = "o"
                display_board()
                break
            else:
                print("that position is already filled")

        check_win(player1)

        while True:
            is_tie()

            value2 = input(f"{player2}, enter the position: ")
            while value2.isalpha() or 0 > int(value2) > 9 or int(value2) <= 0:
                print("enter a numeric value between 1 and 9")
                value2 = input(f"{player2}, enter the position: ")

            value2 = int(value2)
            if cell[value2 - 1] == "-":
                cell[value2 - 1] = "x"
                display_board()
                break
            else:
                print("that position is already filled")

        check_win(player2)


play_game()

