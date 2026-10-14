# no two queen can be in the same row

# no two queen can be in the same column

# no two queen can be in the same diagonal

def solve_n_queens(n):
    board = [-1] * n

    def solve(row):
        if row == n:
            for r in range(n):
                print(" ".join(
                    "Q" if board[r] == c else "."
                    for c in range(n)
                ))
            return True

        for col in range(n):
            safe = True

            for prev_row in range(row):
                if (board[prev_row] == col or
                    abs(board[prev_row] - col) == row - prev_row):
                    safe = False
                    break

            if safe:
                board[row] = col
                if solve(row + 1):
                    return True

        return False

    if not solve(0):
        print("No solution exists")

n = int(input("enter number of quees:"))
solve_n_queens(n)