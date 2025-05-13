import heapq

goal_state = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 0]
]

moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def is_goal(state):
    return state == goal_state

def manhattan_distance(state):
    distance = 0
    for i in range(3):
        for j in range(3):
            value = state[i][j]
            if value != 0:
                goal_x, goal_y = (value - 1) // 3, (value - 1) % 3
                distance += abs(i - goal_x) + abs(j - goal_y)
    return distance

def find_zero(state):
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return i, j

def copy_state(state):
    return [row[:] for row in state]

def get_neighbors(state):
    neighbors = []
    x, y = find_zero(state)
    for dx, dy in moves:
        nx, ny = x + dx, y + dy
        if 0 <= nx < 3 and 0 <= ny < 3:
            new_state = copy_state(state)
            new_state[x][y], new_state[nx][ny] = new_state[nx][ny], new_state[x][y]
            neighbors.append(new_state)
    return neighbors

def serialize(state):
    return str(state)

def a_star(start_state):
    heap = []
    visited = set()
    heapq.heappush(heap, (manhattan_distance(start_state), 0, start_state, []))

    while heap:
        estimated_cost, cost_so_far, current_state, path = heapq.heappop(heap)
        if serialize(current_state) in visited:
            continue
        visited.add(serialize(current_state))

        if is_goal(current_state):
            return path + [current_state]

        for neighbor in get_neighbors(current_state):
            if serialize(neighbor) not in visited:
                heapq.heappush(heap, (
                    cost_so_far + 1 + manhattan_distance(neighbor),
                    cost_so_far + 1,
                    neighbor,
                    path + [current_state]
                ))
    return None

def print_path(path):
    for step, state in enumerate(path):
        print(f"Step {step}:")
        for row in state:
            print(row)
        print()

# Example usage
if __name__ == "__main__":

    start_state = [
        [1, 2, 3],
        [4, 0, 6],
        [7, 5, 8]
    ]

    print("Solving the 8-puzzle problem...\n")
    solution = a_star(start_state)
    if solution:
        print_path(solution)
        print(f"Total steps: {len(solution) - 1}")
    else:
        print("No solution found.")
