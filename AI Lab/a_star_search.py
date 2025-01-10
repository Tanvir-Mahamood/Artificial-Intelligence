import heapq

def a_star_search(graph, src, goal, heuristic):
    pq = []
    heapq.heappush(pq, (0 + heuristic[src], 0, src))  # (f = g + h, g, node)
    visited = set()
    g_cost = {src: 0}  # Stores the cost to reach each node
    parent = {src: None}

    while pq:
        _, current_cost, current = heapq.heappop(pq)

        if current in visited:
            continue

        visited.add(current)

        if current == goal:
            # Reconstruct the path and calculate total distance
            path = []
            while current:
                path.append(current)
                current = parent[current]
            return path[::-1], g_cost[goal]

        for child, weight in graph[current]:
            if child not in visited:
                tentative_g = current_cost + weight
                if child not in g_cost or tentative_g < g_cost[child]:
                    g_cost[child] = tentative_g
                    parent[child] = current
                    f = tentative_g + heuristic[child]
                    heapq.heappush(pq, (f, tentative_g, child))

    return None, -1  # If no path is found


# Example usage
graph = {
    1: [(2, 1), (3, 5), (4, 8)],
    2: [(5, 3), (6, 7), (7, 9)],
    3: [(7, 4)],
    4: [(7, 9)],
    5: [],
    6: [],
    7: []
}
heuristic = {1: 10, 2: 6, 3: 5, 4: 8, 5: 7, 6: 3, 7: 0}  # Example heuristic values
src, goal = 1, 7

path, distance = a_star_search(graph, src, goal, heuristic)
if path:
    print("Path:", "->".join(map(str, path)))
    print("Total Distance:", distance)
else:
    print("No path found.")



