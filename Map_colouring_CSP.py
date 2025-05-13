australia_map = {
    'WA': ['NT', 'SA'],
    'NT': ['WA', 'SA', 'Q'],
    'SA': ['WA', 'NT', 'Q', 'NSW', 'V'],
    'Q': ['NT', 'SA', 'NSW'],
    'NSW': ['Q', 'SA', 'V'],
    'V': ['SA', 'NSW'],
    'T': [] 
}

colors = ['Red', 'Green', 'Blue']

def is_valid(region, color, assignment):
    for neighbor in australia_map[region]:
        if neighbor in assignment and assignment[neighbor] == color:
            return False
    return True

def backtrack(assignment):
    if len(assignment) == len(australia_map):
        return assignment

    unassigned = [r for r in australia_map if r not in assignment][0]

    for color in colors:
        if is_valid(unassigned, color, assignment):
            assignment[unassigned] = color
            result = backtrack(assignment)
            if result:
                return result
            del assignment[unassigned]

    return None

solution = backtrack({})

if solution:
    print("Solution to Map Coloring:")
    for region, color in solution.items():
        print(f"{region}: {color}")
else:
    print("No solution found.")
