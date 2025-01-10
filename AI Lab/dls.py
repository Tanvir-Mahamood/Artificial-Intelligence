def dls(graph, src, limit):
    max_node = max(graph.keys())
    visited = [False] * (max_node + 1)
    parent = [None] * (max_node + 1)
    distance = [-1] * (max_node + 1)  # Distance array initialized to -1

    def dls_recursive(node, current_depth, current_distance):
        if current_depth > limit:
            return  # Stop exploring beyond the depth limit
        
        visited[node] = True
        distance[node] = current_distance
        
        for child, weight in graph[node]:
            if not visited[child]:
                parent[child] = node
                dls_recursive(child, current_depth + 1, current_distance + weight)

    # Start from the source with depth 0 and distance 0
    dls_recursive(src, 0, 0)
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
limit = 2

distance, parent = dls(graph, src, limit)
if distance[end] != -1:
    path = path_construction(parent, end)
    print("->".join(map(str, path)))
    print(f"Total Code: {distance[end]}")

else:
    print("Path not found")
