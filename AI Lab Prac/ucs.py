import heapq

def ucs(graph, src, goal):
    pq = []                       
    heapq.heappush(pq, (0, src))  # (cost, node)
    min_cost = {src: 0}           # Dictionary to store the minimum cost to reach each node

    visited = set()
    parent = {src: None} 
    total_distance = 0

    while pq:
        current_cost, current_node = heapq.heappop(pq)
        # print(f"{parent[current_node]} {current_node}")
        if current_node in visited:
            continue

        visited.add(current_node)

        if current_node == goal:
            total_distance = current_cost
            break

        
        for child, weight in graph[current_node]:
            new_cost = current_cost + weight
            if child not in min_cost or new_cost < min_cost[child]:
                min_cost[child] = new_cost
                parent[child] = current_node
                heapq.heappush(pq, (new_cost, child))
        
        """for child, weight in graph[current_node]:
            parent[child] = current_node
            print(f"parent: {parent[child]} and child: {child}")
            heapq.heappush(pq, (current_cost+weight, child))"""

    
    # Reconstruct path
    path = []
    current = goal
    while current is not None:
        path.append(current)
        current = parent[current]
    path.reverse()

    return path, total_distance


graph = {
    'S': [('A', 2), ('B', 3), ('C', 5)],
    'A': [('E', 1)],
    'B': [('D', 1)],
    'C': [('H', 3)],
    'D': [('G', 1)],
    'E': [('G', 2)],
    'G': [],
    'H': []
}

src = 'S'
end = 'G'

path, distance = ucs(graph, src, end)
print(f"Path: {' -> '.join(path)}")
print(f"Total Code: {distance}")