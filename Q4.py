# Q.4. Implement Depth First Search (for Water Jug problem). 

def dfs_water_jug(capacity1, capacity2, target):
    
    stack = [(0, 0, [])]
    visited = set()

    while stack:
        jug1, jug2, path = stack.pop()

        if (jug1, jug2) in visited:
            continue

        visited.add((jug1, jug2))
        path = path + [(jug1, jug2)]

        # Check if target is reached

        if jug1 == target or jug2 == target:
            return path

        # Generate possible states

        # Fill Jug 1
        states = [
            (capacity1, jug2),

            # Fill Jug 2
            (jug1, capacity2),

            # Empty Jug 1
            (0, jug2),

            # Empty Jug 2
            (jug1, 0),

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

        # Add states to stack

        for state in states:

            if state not in visited:
                stack.append((state[0], state[1], path))

    return None


# Jug capacities

capacity1 = 4
capacity2 = 3

# Required amount
target = 2

# Apply DFS
solution = dfs_water_jug(capacity1, capacity2, target)

if solution:
    print("Solution found!\n")

    for step, state in enumerate(solution):
        print("Step", step, ":", state)
else:
    print("No solution exists.")