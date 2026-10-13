# Q. 2. Implement Breadth First Search (for Water Jug problem). 

from collections import deque

def water_jug_bfs(capacity1, capacity2, target):
    
    queue = deque()
    visited = set()

    # Initial state: both jugs are empty
    queue.append((0, 0, []))

    while queue:
        jug1, jug2, path = queue.popleft()

        if (jug1, jug2) in visited:
            continue

        visited.add((jug1, jug2))

        # Store current state
        path = path + [(jug1, jug2)]

        # Check if target is reached

        if jug1 == target or jug2 == target:
            return path

        # Generate all possible states

        states = [
            (capacity1, jug2),  # Fill Jug 1
            (jug1, capacity2),  # Fill Jug 2

            (0, jug2),          # Empty Jug 1
            (jug1, 0),          # Empty Jug 2

            # Pour Jug 1 -> Jug 2
            (
                jug1 - min(jug1, capacity2 - jug2),
                jug2 + min(jug1, capacity2 - jug2)
            ),

            # Pour Jug 2 -> Jug 1
            (
                jug1 + min(jug2, capacity1 - jug1),
                jug2 - min(jug2, capacity1 - jug1)
            )
        ]

        for state in states:
            if state not in visited:
                queue.append((state[0], state[1], path))

    return None


# Jug capacities

capacity1 = 4
capacity2 = 3

# Required amount
target = 2

solution = water_jug_bfs(capacity1, capacity2, target)

if solution:
    print("Solution found:\n")

    for step, state in enumerate(solution):
        print("Step", step, ":", state)

else:
    print("No solution exists.")