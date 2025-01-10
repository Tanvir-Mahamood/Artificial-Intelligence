from collections import deque

def bfs(graph, src):
    src_idx = ord(src) - ord('A')
    visited = [False] * 26
    distance = [-1] * 26
    parent = [None] * 26

    q = deque([src])
    visited[src_idx] = True
    distance[src_idx] = 0

    while q:
        node = q.popleft()
        for child in graph[node]:
            child_idx = ord(child) - ord('A')
            if not visited[child_idx]:
                q.append(child)
                visited[child_idx] = True
                distance[child_idx] = distance[ord(node)-ord('A')] + 1
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
    'S': ['A', 'B', 'C'],
    'A': ['D', 'E', 'S'],
    'B': ['F', 'S'],
    'C': ['H', 'S'],
    'D': ['A'],
    'E': ['A', 'G'],
    'F': ['B', 'G'],
    'H': ['C', 'G'],
    'G': ['E', 'F', 'H']
}
src = 'S'
end = 'G'

distance, parent = bfs(graph, src)

print()
path = path_construction(parent, end)
for node in path:
    print(node, end="->")

print(f"Total Code: {distance[ord(end) - ord('A')]}")


