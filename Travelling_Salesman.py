import itertools

def calculate_total_distance(route, dist_matrix):
    total_distance = 0
    for i in range(len(route) - 1):
        total_distance += dist_matrix[route[i]][route[i + 1]]
    total_distance += dist_matrix[route[-1]][route[0]] 
    return total_distance

def travelling_salesman(dist_matrix):
    n = len(dist_matrix)
    cities = range(n)
    
    all_routes = itertools.permutations(cities)
    
    best_route = None
    min_distance = float('inf')
    
    for route in all_routes:
        total_distance = calculate_total_distance(route, dist_matrix)
        if total_distance < min_distance:
            min_distance = total_distance
            best_route = route
    
    return best_route, min_distance

dist_matrix = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]

best_route, min_distance = travelling_salesman(dist_matrix)

print("Best route:", best_route)
print("Minimum distance:", min_distance)
