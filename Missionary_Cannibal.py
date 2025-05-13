from collections import deque
    
initial_state = (3, 3, 1)
goal_state = (0, 0, 0)

def is_valid(m, c):
    return (m == 0 or m >= c) and (3 - m == 0 or (3 - m) >= (3 - c))

def get_successors(state):
    m, c, b = state
    moves = [(1, 0), (2, 0), (0, 1), (0, 2), (1, 1)]
    successors = []

    for dm, dc in moves:
        if b == 1:
            new_m, new_c, new_b = m - dm, c - dc, 0
        else:
            new_m, new_c, new_b = m + dm, c + dc, 1

        if 0 <= new_m <= 3 and 0 <= new_c <= 3 and is_valid(new_m, new_c):
            successors.append((new_m, new_c, new_b))
    return successors

def solve():
    queue = deque([(initial_state, [initial_state])])
    visited = set()

    while queue:
        state, path = queue.popleft()

        if state == goal_state:
            return path

        for successor in get_successors(state):
            if successor not in visited:
                visited.add(successor)
                queue.append((successor, path + [successor]))
    return None

solution = solve()
if solution:
    print("Solution found in", len(solution)-1, "moves:")
    for step in solution:
        print(step)
else:
    print("No solution found.")
