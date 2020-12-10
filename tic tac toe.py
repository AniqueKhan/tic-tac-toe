# Creating A TIC TAC TOE Game In Python
board = [" " for x in range(10)]


def insert_letter(letter, pos):
    board[pos] = letter


def space_is_free(pos):
    return board[pos] == " "


def ver_lines():
    print("   |   |")


def hor_lines():
    print("-----------")


def spaces_in_the_board(board, a, b, c):
    print(" " + board[a] + " | " + board[b] + " | " + board[c])


def print_board(board):
    ver_lines()
    spaces_in_the_board(board, 1, 2, 3)
    ver_lines()
    hor_lines()
    ver_lines()
    spaces_in_the_board(board, 4, 5, 6)
    ver_lines()
    hor_lines()
    ver_lines()
    spaces_in_the_board(board, 7, 8, 9)
    ver_lines()


def is_board_full(board):
    if board.count(" ") > 1:
        return False
    else:
        return True


def select_random(any_list):
    import random
    ln = len(any_list)
    r = random.randrange(0, ln)
    return any_list[r]


def is_winner(bo, le):  # bo stands for board and le stands for letter
    return (bo[1] == le and bo[2] == le and bo[3] == le) or (bo[4] == le and bo[5] == le and bo[6] == le) or (
            bo[7] == le and bo[8] == le and bo[9] == le) or (bo[1] == le and bo[4] == le and bo[7] == le) or (
                   bo[2] == le and bo[5] == le and bo[8] == le) or (bo[3] == le and bo[6] == le and bo[9] == le) or (
                   bo[1] == le and bo[5] == le and bo[9] == le) or (bo[3] == le and bo[5] == le and bo[7] == le)


def player_move():
    run = True
    while run:
        move = input("Please insert a position to place an 'X' (1-9): ")
        try:
            move = int(move)
            if 0 < move < 10:
                if space_is_free(move):
                    run = False
                    insert_letter("X", move)
                else:
                    print("This position is already occupied")
            else:
                print("Please insert a number within the range")
        except:
            print("Please insert a number")


def computer_move():
    possible_moves = [x for x, letter in enumerate(board) if letter == " " and x != 0]
    move = 0
    for let in ["O", "X"]:
        for i in possible_moves:
            board_copy = board[:]
            board_copy[i] = let
            while is_winner(board_copy, let):
                move = i
                return move
    corners_open = []
    for i in possible_moves:
        if i in [1, 3, 7, 9]:
            corners_open.append(i)
    if len(corners_open) > 0:
        move = select_random(corners_open)
        return move
    if 5 in possible_moves:
        move = 5
        return move
    edges_open = []
    for i in possible_moves:
        if i in [1, 3, 7, 9]:
            edges_open.append(i)
    if len(edges_open) > 0:
        move = select_random(edges_open)
    return move


def main():
    print("Welcome to the TIC TAC TOE! I'm assuming you already\nknow the rules so let's jump right into it!!!")
    print_board(board)
    while not (is_board_full(board)):
        if not (is_winner(board, "O")):
            player_move()
            print_board(board)
        else:
            print("Sorry, you lost the game.Try again!")
            break
        if not (is_winner(board, "X")):
            move = computer_move()
            if move == 0:
                print("Tie Game")
            else:
                insert_letter("O", move)
                print("The computer placed an 'O' at", move)
                print_board(board)
        else:
            print("Great Job.You win!")
            break
    if is_board_full(board):
        print("Tie Game")


while True:
    ans = input("Do you want to play Tic Tac Toe? (Y/N): ")
    if ans.lower() == "y" or ans.lower() == "yes":
        board = [" " for x in range(10)]
        print("----------------------------")
        main()
    else:
        break
