from collections import deque

def bfs(graph, start):
    n = len(graph)  
    visited = [False] * (n+ 1)
    distance = [-1] * (n + 1)
    queue = deque([start])
    
    visited[start] = True
    distance[start] = 0

    while queue:
        node = queue.popleft()
        print(node, end="->")
        for child in range(n):
            if graph[node-1][child] == 1 and not visited[child+1]:
                queue.append(child+1)
                visited[child+1] = True
                distance[child+1] = distance[node] + 1

    return distance


# (a) Adjacency matrix, defined in code
"""
graph = [
    [0, 1, 1, 0, 0, 0],  # Node 1
    [1, 0, 0, 1, 1, 0],  # Node 2
    [1, 0, 0, 0, 0, 1],  # Node 3
    [0, 1, 0, 0, 0, 0],  # Node 4
    [0, 1, 0, 0, 0, 1],  # Node 5
    [0, 0, 1, 0, 1, 0]   # Node 6
]

"""

# (b) User Input Adjacency matrix:
n = int(input("Enter the number of nodes: "))
graph = []

print("Enter the adjacency matrix row by row:")
for i in range(n):
    row = list(map(int, input().split()))
    graph.append(row)




print("BFS: ")
distance = bfs(graph, 1)
print()
n = len(graph)
for i in range(1, n+1):
        print(f"Node {i}: Distance {distance[i]}")
