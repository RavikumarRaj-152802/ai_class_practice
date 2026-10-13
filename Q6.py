# Q.6 Write a program to implement Single Player Game (Using Heuristic Function). 

import heapq

def heuristic(state, goal):
    distance = 0

    for i in range(9):
        if state[i] != 0:
            goal_pos = goal.index(state[i])
            x1, y1 = divmod(i, 3)
            x2, y2 = divmod(goal_pos, 3)
            distance += abs(x1 - x2) + abs(y1 - y2)

    return distance


def get_neighbors(state):
    neighbors = []
    zero = state.index(0)
    x, y = divmod(zero, 3)

    moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    for dx, dy in moves:
        nx, ny = x + dx, y + dy

        if 0 <= nx < 3 and 0 <= ny < 3:
            new_pos = nx * 3 + ny
            new_state = state[:]
            new_state[zero], new_state[new_pos] = (
                new_state[new_pos], new_state[zero]
            )
            neighbors.append(new_state)

    return neighbors


def solve(start, goal):
    pq = [(heuristic(start, goal), 0, start, [])]
    visited = set()

    while pq:
        f, g, state, path = heapq.heappop(pq)
        key = tuple(state)

        if key in visited:
            continue

        visited.add(key)
        path = path + [state]

        if state == goal:
            return path

        for neighbor in get_neighbors(state):
            if tuple(neighbor) not in visited:
                new_g = g + 1
                new_f = new_g + heuristic(neighbor, goal)
                heapq.heappush(
                    pq, (new_f, new_g, neighbor, path)
                )

    return None


start = [1, 2, 3,
         4, 0, 6,
         7, 5, 8]

goal = [1, 2, 3,
        4, 5, 6,
        7, 8, 0]

solution = solve(start, goal)

if solution:
    print("Solution found!")
    print("Number of moves:", len(solution) - 1)

    for state in solution:
        for i in range(0, 9, 3):
            print(state[i:i + 3])
        print()
else:
    print("No solution exists.")