# Two-player game - Tic-Tac-Toe
# Using a heuristic function

# Display the board
def display(board):
    print()
    print(board[0], "|", board[1], "|", board[2])
    print("--|---|--")
    print(board[3], "|", board[4], "|", board[5])
    print("--|---|--")
    print(board[6], "|", board[7], "|", board[8])
    print()


# Heuristic function
def heuristic(board):
    win = [
        (0, 1, 2),
        (3, 4, 5),
        (6, 7, 8),
        (0, 3, 6),
        (1, 4, 7),
        (2, 5, 8),
        (0, 4, 8),
        (2, 4, 6)
    ]

    for a, b, c in win:
        if board[a] == board[b] == board[c] == "x":
            return 10
        elif board[a] == board[b] == board[c] == "o":
            return -10

    return 0


# Main game
board = [" "] * 9
player = "x"

for turn in range(9):
    display(board)
    print("Player", player.upper())

    try:
        position = int(input("Enter position (1-9): ")) - 1
    except ValueError:
        print("Please enter a valid number.")
        continue

    if position < 0 or position > 8 or board[position] != " ":
        print("Invalid position! Try again.")
        continue

    board[position] = player

    # Check the winner
    score = heuristic(board)

    if score == 10:
        display(board)
        print("Player X wins!")
        break

    if score == -10:
        display(board)
        print("Player O wins!")
        break

    # Change player
    if player == "x":
        player = "o"
    else:
        player = "x"

else:
    display(board)
    print("Game draw!")