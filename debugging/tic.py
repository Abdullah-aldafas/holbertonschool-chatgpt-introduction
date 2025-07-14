# ✅ Solved: Task 6 - Fixed logic and input handling in Tic Tac Toe
# - Fixed winner message to show correct player
# - Added input validation and error handling
# - Added draw detection when the board is full

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board):
    # Check rows
    for row in board:
        if row.count(row[0]) == 3 and row[0] != " ":
            return True

    # Check columns
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
            return True

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return True

    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return True

    return False

def is_full(board):
    for row in board:
        if " " in row:
            return False
    return True

def tic_tac_toe():
    board = [[" "]*3 for _ in range(3)]
    player = "X"

    while True:
        print_board(board)

        # Input with validation
        try:
            row = int(input("Enter row (0, 1, or 2) for player " + player + ": "))
            col = int(input("Enter column (0, 1, or 2) for player " + player + ": "))
            if not (0 <= row < 3 and 0 <= col < 3):
                print("Invalid position. Please enter numbers between 0 and 2.")
                continue
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if board[row][col] != " ":
            print("That spot is already taken! Try again.")
            continue

        board[row][col] = player

        if check_winner(board):
            print_board(board)
            print("Player " + player + " wins!")
            break

        if is_full(board):
            print_board(board)
            print("It's a draw!")
            break

        player = "O" if player == "X" else "X"

tic_tac_toe()
