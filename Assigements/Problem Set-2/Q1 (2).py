def dfs(node, parent, direction, graph, visited):
    visited[node] = True
    
    for neighbor in graph[node]:
        if not visited[neighbor]:
            direction[node][neighbor] = 1  # Direction from node to neighbor
            direction[neighbor][node] = 0  # Direction from neighbor to node
            dfs(neighbor, node, direction, graph, visited)

# Read input
N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]  # Create a graph with N+1 nodes (1-based indexing)
for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

# Initialize data structures
direction = [[-1] * (N + 1) for _ in range(N + 1)]
visited = [False] * (N + 1)

# Perform DFS from any node to assign directions
dfs(1, 0, direction, graph, visited)

# Check if all nodes have even indegrees
for i in range(1, N + 1):
    if len(graph[i]) % 2 != sum(direction[i]):
        print("-1")
        exit()

# Print the directions of the edges
for i in range(1, N + 1):
    for j in graph[i]:
        print(direction[i][j], end=" ")
print()