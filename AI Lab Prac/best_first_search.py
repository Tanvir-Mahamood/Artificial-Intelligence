import heapq

def best_first_search(graph, heuristics, start, goal):
    pq = [] 
    heapq.heappush(pq, (heuristics[start], 0, start))  # (heuristic value, distance from start, node)
    visited = set()
    parent = {start: None}

    while pq:
        current_h, current_distance, current_node = heapq.heappop(pq)

        if current_node in visited:
            continue

        visited.add(current_node)

        if current_node == goal:
            path = []
            while current_node is not None:
                path.append(current_node)
                current_node = parent[current_node]
            path.reverse()
            return current_distance, path

        for child, weight in graph[current_node]:
            if child not in visited:
                parent[child] = current_node
                heapq.heappush(pq, (heuristics[child], current_distance + weight, child))

    return None, None 


graph = {
    'S': [('A', 2), ('B', 3), ('C', 5)],
    'A': [('E', 1)],
    'B': [('D', 1)],
    'C': [('H', 3)],
    'D': [('G', 1)],
    'E': [('G', 3)],
    'G': [],
    'H': []
}

heuristics = { 'S': 10, 'A': 7, 'B': 3, 'C': 11, 'D': 2, 'E': 3, 'G': 0, 'H': 10000 }

start = 'S'
goal = 'G'

distance, path = best_first_search(graph, heuristics, start, goal)
if path:
    print(f"Path: {' -> '.join(path)}")
    print(f"Total Distance: {distance}")
else:
    print("No path found.")
