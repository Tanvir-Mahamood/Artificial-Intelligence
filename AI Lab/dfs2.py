def dfs(graph, src):
    n = len(graph)
    visited = [False] * (n + 1)
    distance = [-1] * (n + 1)

    def dfs_recursive(node):
          visited[node] = True
          print(node, end="->")
          for child in range(n):
                if graph[node-1][child] == 1 and not visited[child+1]:
                      dfs_recursive(child+1)
    
    distance[src] = 0
    dfs_recursive(src)
    return distance


# (a) Adjacency matrix, defined in code

graph = [
    [0, 1, 1, 0, 0, 0],  # Node 1
    [1, 0, 0, 1, 1, 0],  # Node 2
    [1, 0, 0, 0, 0, 1],  # Node 3
    [0, 1, 0, 0, 0, 0],  # Node 4
    [0, 1, 0, 0, 0, 1],  # Node 5
    [0, 0, 1, 0, 1, 0]   # Node 6
]



# (b) User Input Adjacency matrix:
"""
n = int(input("Enter the number of nodes: "))
graph = []

print("Enter the adjacency matrix row by row:")
for i in range(n):
    row = list(map(int, input().split()))
    graph.append(row)

"""


print("DFS: ")
distance = dfs(graph, 1)
print()
n = len(graph)
for i in range(1, n+1):
        print(f"Node {i}: Distance {distance[i]}")
