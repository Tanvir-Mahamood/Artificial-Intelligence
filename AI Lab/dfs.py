def dfs(graph, src):
    max_node = max(graph.keys())
    visited = [False] * (max_node + 1)
    distance = [-1] * (max_node + 1)

    def dfs_recursive(node):
        visited[node] = True
        print(node, end="->")
        for child in graph[node]:
            if not visited[child]:
                distance[child] = distance[node] + 1
                dfs_recursive(child)
        

    distance[src] = 0
    dfs_recursive(src)
    return distance


# Graph Input:
# (a) Adjacency list, declared in code:
#----------------------------------------
"""
graph = {
    1: [2, 3],
    2: [1, 4, 5],
    3: [1, 6],
    4: [2],
    5: [2],
    6: [3]
}
"""


# (b) Adjacency list from user input
"""
n = int(input("Enter the number of nodes: "))
graph = {}
for i in range(1, n+1):
    edges = list(map(int, input(f"Enter neighbors of node {i} (space-separated): ").split()))
    graph[i] = edges
"""



# (c) Constructing from adjacency list

n = int(input("Enter the number of nodes: "))
m = int(input("Enter the number of edges: "))
graph = {i: [] for i in range(1, n + 1)}

for _ in range(m):
    u, v = map(int, input("Enter edge (u v): ").split())
    graph[u].append(v)
    graph[v].append(u)





print("DFS: ")
distance = dfs(graph, 1)
print()
n = max(graph.keys())
for i in range(1, n+1):
    print(f"Node: {i}, distance: {distance[i]}")