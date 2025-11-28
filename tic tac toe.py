# Tic Tac Toe game using basic Python

# Function to display the board
def print_board(board):
    print("\n")
    for i in range(3):
        print(board[3*i] + " | " + board[3*i+1] + " | " + board[3*i+2])
        if i < 2:
            print("--+---+--")
    print("\n")

# Function to check if a player has won
def check_winner(board, player):
    win_conditions = [
        [0,1,2], [3,4,5], [6,7,8],  # rows
        [0,3,6], [1,4,7], [2,5,8],  # columns
        [0,4,8], [2,4,6]            # diagonals
    ]
    for condition in win_conditions:
        if all(board[i] == player for i in condition):
            return True
    return False

# Main game function
def tic_tac_toe():
    board = [" " for _ in range(9)]  # empty board
    current_player = "X"

    for turn in range(9):  # maximum 9 moves
        print_board(board)
        print(f"Player {current_player}, choose your move (1-9): ")

        # take input
        move = int(input()) - 1  

        # check valid move
        if board[move] != " ":
            print("Invalid move! Try again.")
            continue

        # make the move
        board[move] = current_player

        # check winner
        if check_winner(board, current_player):
            print_board(board)
            print(f"🎉 Player {current_player} wins!")
            return

        # switch player
        current_player = "O" if current_player == "X" else "X"

    # if loop finishes → draw
    print_board(board)
    print("It's a draw!")

# Run the game
tic_tac_toe()
