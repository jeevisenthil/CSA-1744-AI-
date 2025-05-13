from collections import deque

def water_jug_problem(jug1_capacity, jug2_capacity, target):
    visited = set()
    q = deque()

    q.append(((0, 0), []))

    while q:
        (jug1, jug2), path = q.popleft()

        # If already visited, skip
        if (jug1, jug2) in visited:
            continue
        visited.add((jug1, jug2))

        # Add current state to path
        path = path + [((jug1, jug2))]

        # Check if we have reached the target
        if jug1 == target or jug2 == target:
            print("Solution found!")
            for step in path:
                print(f"Jug1: {step[0]} | Jug2: {step[1]}")
            return

        # Generate all possible next states
        possible_states = [
            (jug1_capacity, jug2),            
            (jug1, jug2_capacity),            
            (0, jug2),                        
            (jug1, 0),                     
            (0, jug1 + jug2) if jug1 + jug2 <= jug2_capacity else (jug1 - (jug2_capacity - jug2), jug2_capacity),
            (jug1 + jug2, 0) if jug1 + jug2 <= jug1_capacity else (jug1_capacity, jug2 - (jug1_capacity - jug1)),
        ]

        for state in possible_states:
            if state not in visited:
                q.append((state, path))

    print("No solution found.")

if __name__ == "__main__":
    jug1_capacity = 4
    jug2_capacity = 3
    target = 2
    water_jug_problem(jug1_capacity, jug2_capacity, target)
