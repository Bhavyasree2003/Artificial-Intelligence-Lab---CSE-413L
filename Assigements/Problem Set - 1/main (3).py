from collections import defaultdict, deque

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
    
    def add_edge(self, u, v):
        self.graph[u].append(v)
    
    def bfs(self, start):
        visited = set()
        queue = deque([start])
        traversal = []

        while queue:
            vertex = queue.popleft()
            if vertex not in visited:
                traversal.append(vertex)
                visited.add(vertex)
                queue.extend(self.graph[vertex])

        return traversal
    
    def dfs_util(self, vertex, visited, traversal):
        visited.add(vertex)
        traversal.append(vertex)
        
        for neighbor in self.graph[vertex]:
            if neighbor not in visited:
                self.dfs_util(neighbor, visited, traversal)
    
    def dfs(self, start):
        visited = set()
        traversal = []
        self.dfs_util(start, visited, traversal)
        return traversal
    
    def topological_sort_util(self, vertex, visited, stack):
        visited.add(vertex)
        
        for neighbor in self.graph[vertex]:
            if neighbor not in visited:
                self.topological_sort_util(neighbor, visited, stack)
        
        stack.insert(0, vertex)
    
    def topological_sort(self):
        visited = set()
        stack = []
        
        for vertex in self.graph:
            if vertex not in visited:
                self.topological_sort_util(vertex, visited, stack)
        
        return stack

# Example usage
g = Graph()
g.add_edge('A', 'B')
g.add_edge('A', 'C')
g.add_edge('B', 'D')
g.add_edge('C', 'E')
g.add_edge('D', 'E')

bfs_traversal = g.bfs('A')
dfs_traversal = g.dfs('A')
topological_order = g.topological_sort()

print("BFS Traversal:", bfs_traversal)
print("DFS Traversal:", dfs_traversal)
print("Topological Order:", topological_order)
