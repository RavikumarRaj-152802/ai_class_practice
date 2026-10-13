# Q.8 Write a program to solve N-Queens problem. 

def print_board(board, n):
    for i in range(n):
        for j in range(n):
            if board[i] == j:
                print("Q", end=" ")
            else:
                print(".", end=" ")
        print()


def is_safe(board, row, col):
    for i in range(row):
        if board[i] == col:
            return False

        if abs(board[i] - col) == abs(i - row):
            return False

    return True


def solve_n_queens(board, row, n):
    if row == n:
        print_board(board, n)
        return True

    found = False

    for col in range(n):
        if is_safe(board, row, col):
            board[row] = col

            if solve_n_queens(board, row + 1, n):
                found = True

            board[row] = -1

    return found


n = int(input("Enter the value of N: "))
board = [-1] * n

if n <= 0:
    print("Enter a positive integer.")
    
elif not solve_n_queens(board, 0, n):
    print("No solution exists.")