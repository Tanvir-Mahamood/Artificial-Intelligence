def ids(graph, src, max_depth):
    max_node = max(graph.keys())
    distance = [-1] * (max_node + 1)  # Initialize distances to -1
    parent = [None] * (max_node + 1)

    def dls_recursive(node, current_depth, current_distance, visited):
        if current_depth > max_depth:
            return  # Stop exploring beyond the current depth limit

        visited[node] = True
        if distance[node] == -1 or current_distance < distance[node]:
            distance[node] = current_distance
        
        for child, weight in graph[node]:
            if not visited[child]:
                parent[child] = node
                dls_recursive(child, current_depth + 1, current_distance + weight, visited)

    def dls_with_limit(limit):
        visited = [False] * (max_node + 1)
        dls_recursive(src, 0, 0, visited)

    for depth in range(max_depth + 1):
        print(f"Depth: {depth}")
        dls_with_limit(depth)
        print("Current distances:", distance)
    
    return distance, parent


def path_construction(parent, end):
    path = []
    current = end
    while current is not None:
        path.append(current)
        if parent[current] is None:
            break
        current = parent[current]
    return path[::-1]  


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

src = 1
end = 7
max_depth = 3

distance, parent = ids(graph, src, max_depth)
path = path_construction(parent, end)
print("->".join(map(str, path)))
print(f"Total Code: {distance[end]}")
