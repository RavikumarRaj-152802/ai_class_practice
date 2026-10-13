# Q.3. Implement Depth First Search (for 8 puzzle problem). 

def dfs(start, goal):
    stack = [(start, [])]
    visited = {tuple(start)}

    moves = [
        (-1, 0),  # Up
        (1, 0),   # Down
        (0, -1),  # Left
        (0, 1)    # Right
    ]

    while stack:
        state, path = stack.pop()

        if state == goal:
            return path + [state]

        zero = state.index(0)
        x, y = divmod(zero, 3)

        for dx, dy in moves:
            nx, ny = x + dx, y + dy

            if 0 <= nx < 3 and 0 <= ny < 3:
                new_zero = nx * 3 + ny
                new_state = state[:]

                new_state[zero], new_state[new_zero] = (
                    new_state[new_zero], new_state[zero]
                )

                key = tuple(new_state)

                if key not in visited:
                    visited.add(key)
                    stack.append((new_state, path + [state]))

    return None


# 0 represents the blank tile
start = [1, 2, 3,
         4, 0, 6,
         7, 5, 8]

goal = [1, 2, 3,
        4, 5, 6,
        7, 8, 0]

solution = dfs(start, goal)

if solution:
    print("Solution found!")
    print("Number of moves:", len(solution) - 1)

    for state in solution:
        for i in range(0, 9, 3):
            print(state[i:i + 3])
        print()
else:
    print("No solution exists.")