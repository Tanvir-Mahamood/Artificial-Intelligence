from collections import deque

def bfs(graph, src):
    src_idx = ord(src) - ord('A')
    visited = [False] * 26
    distance = [-1] * 26
    parent = [None] * 26

    q = deque([(src, 0)])
    visited[src_idx] = True
    distance[src_idx] = 0

    while q:
        node, current_distance = q.popleft()
        for child, weight in graph[node]:
            child_idx = ord(child) - ord('A')
            if not visited[child_idx]:
                q.append((child, current_distance+weight))
                visited[child_idx] = True
                distance[child_idx] = current_distance + weight
                parent[child_idx] = node
    return distance, parent


def path_construction(parent, end):
    path = []
    current = ord(end) - ord('A')
    while current is not None:
        path.append(chr(current + ord('A')))
        if parent[current] is None:
            break
        current = ord(parent[current]) - ord('A')
    return path[::-1]  


# Graph Input:
# (a) Adjacency list, declared in code:
#----------------------------------------
graph = {
    'S': [('A', 2), ('B', 1), ('C', 3)],
    'A': [('D', 3), ('E', 4), ('S', 2)],
    'B': [('F', 6), ('S', 1)],
    'C': [('H', 1), ('S', 3)],
    'D': [('A', 3)],
    'E': [('A', 4), ('G', 9)],
    'F': [('B', 6), ('G', 7)],
    'H': [('C', 1), ('G', 2)],
    'G': [('E', 9), ('F', 7), ('H', 2)]
}
src = 'S'
end = 'G'

distance, parent = bfs(graph, src)

path = path_construction(parent, end)

print(" -> ".join(path))

print(f"Total Code: {distance[ord(end) - ord('A')]}")


