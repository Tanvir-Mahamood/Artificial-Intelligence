import heapq

def a_star_search(graph, heuristics, start, goal):
    pq = [] 
    heapq.heappush(pq, (0 + heuristics[start], 0, start))  # (f(n), g(n), node)
    visited = set()
    parent = {start: None} 

    while pq:
        current_f, current_g, current_node = heapq.heappop(pq)

        if current_node in visited:
            continue

        visited.add(current_node)

        if current_node == goal:
            path = []
            while current_node is not None:
                path.append(current_node)
                current_node = parent[current_node]
            path.reverse()
            return current_g, path
        
        for child, weight in graph[current_node]:
            if child not in visited:
                g_cost = current_g + weight  
                f_cost = g_cost + heuristics[child]  # f(n) = g(n) + h(n)
                parent[child] = current_node
                # print(f"parent: {parent[child]} and child: {child}")
                heapq.heappush(pq, (f_cost, g_cost, child))

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

distance, path = a_star_search(graph, heuristics, start, goal)
if path:
    print(f"Path: {' -> '.join(path)}")
    print(f"Total Distance: {distance}")
else:
    print("No path found.")
