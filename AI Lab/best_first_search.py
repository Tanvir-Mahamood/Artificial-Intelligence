import heapq

def best_first_search(graph, src, goal, heuristic):
    pq = []
    heapq.heappush(pq, (heuristic[src], src, 0))  # (heuristic value, node, distance)
    visited = set()
    path = []
    total_distance = 0

    while pq:
        _, current, distance = heapq.heappop(pq)

        if current in visited:
            continue

        visited.add(current)
        path.append(current)

        if current == goal:
            total_distance = distance
            break

        for child, weight in graph[current]:
            if child not in visited:
                heapq.heappush(pq, (heuristic[child], child, distance+weight))

    return path, total_distance

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

path, distance = best_first_search(graph, src, goal, heuristic)
print("->".join(map(str, path)))
print(f"Distance: {distance}")
