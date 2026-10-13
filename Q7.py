# Q.7 Implement Two Player Game - Tic-Tac-Toe (Using Heuristic Function). 

board = [' '] * 9

def display_board():
    print()
    for i in range(0, 9, 3):
        print(" " + " | ".join(board[i:i+3]))
        if i < 6:
            print("---+---+---")
    print()

def check_winner(player):
    win_positions = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),
        (0, 3, 6), (1, 4, 7), (2, 5, 8),
        (0, 4, 8), (2, 4, 6)
    ]

    for a, b, c in win_positions:
        if board[a] == board[b] == board[c] == player:
            return True
    return False

def heuristic(player):
    opponent = 'O' if player == 'X' else 'X'
    score = 0

    win_positions = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),
        (0, 3, 6), (1, 4, 7), (2, 5, 8),
        (0, 4, 8), (2, 4, 6)
    ]

    for line in win_positions:
        values = [board[i] for i in line]

        if opponent not in values:
            score += 10 ** values.count(player)

        if player not in values:
            score -= 10 ** values.count(opponent)

    return score

def computer_move():
    best_score = float('-inf')
    best_move = None

    for i in range(9):
        if board[i] == ' ':
            board[i] = 'O'

            if check_winner('O'):
                board[i] = ' '
                return i

            score = heuristic('O')
            board[i] = ' '

            if score > best_score:
                best_score = score
                best_move = i

    return best_move

def play_game():
    print("Tic-Tac-Toe")
    print("You are X; Computer is O.")
    print("Positions are numbered 1 to 9:")
    print("1 | 2 | 3")
    print("--+---+--")
    print("4 | 5 | 6")
    print("--+---+--")
    print("7 | 8 | 9")

    while True:
        display_board()

        try:
            move = int(input("Enter your move (1-9): ")) - 1
        except ValueError:
            print("Enter a valid number.")
            continue

        if move < 0 or move > 8 or board[move] != ' ':
            print("Invalid move! Try again.")
            continue

        board[move] = 'X'

        if check_winner('X'):
            display_board()
            print("You win!")
            break

        if ' ' not in board:
            display_board()
            print("It's a draw!")
            break

        move = computer_move()
        board[move] = 'O'
        print("Computer chooses position", move + 1)

        if check_winner('O'):
            display_board()
            print("Computer wins!")
            break

        if ' ' not in board:
            display_board()
            print("It's a draw!")
            break

play_game()