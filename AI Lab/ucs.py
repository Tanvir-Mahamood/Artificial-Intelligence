import heapq

def ucs(graph, src):
    pq = []                       # Priority Queue, to store nodes with their cumulative cost
    heapq.heappush(pq, (0, src))  # (cost, node)
    min_cost = {src: 0}           # Dictionary to store the minimum cost to reach each node = distance

    max_node = max(graph.keys())
    visited = [False] * (max_node + 1)
    parent = [None] * (max_node + 1)

    while pq:
        current_cost, current_node = heapq.heappop(pq)
        if visited[current_node]:
            continue

        visited[current_node] = True

        for child, weight in graph[current_node]:
            if not visited[child]:
                new_cost = current_cost + weight
                if child not in min_cost or new_cost < min_cost[child]:
                    min_cost[child] = new_cost
                    heapq.heappush(pq, (new_cost, child))
                    parent[child] = current_node

    return min_cost, parent

def path_construction(parent, end):
    path = []
    current = end
    while current is not None:
        path.append(current)
        if parent[current] is None:
            break
        current = parent[current]
    return path[::-1]  

graph = {
    1: [(2, 1), (3, 5), (4, 8)],
    2: [(5, 3), (6, 7), (7, 9)],
    3: [(7, 4)],
    4: [(7, 9)],
    5: [],
    6: [],
    7: []
}

src = 1
end = 7

distance, parent = ucs(graph, src)
path = path_construction(parent, end)
print("->".join(map(str, path)))
print(f"Total Code: {distance[end]}")