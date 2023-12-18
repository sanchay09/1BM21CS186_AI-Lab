from collections import defaultdict

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = defaultdict(list)

    def addEdge(self, u, v):
        self.graph[u].append(v)

    def DLS(self, src, target, maxDepth, path):
        path.append(src)  # Append the current node to the path
        if src == target:
            return True, path
        if maxDepth <= 0:
            return False, path
        for i in self.graph[src]:
            result, path = self.DLS(i, target, maxDepth - 1, path)
            if result:
                return True, path
        path.pop()  # Remove the current node from the path if the target is not found at this level
        return False, path

    def IDDFS(self, src, target, maxDepth):
        for i in range(maxDepth):
            path = []  # Initialize an empty path for each iteration
            result, path = self.DLS(src, target, i, path)
            if result:
                return True, path
        return False, []

# Create a graph based on user input
n = int(input("Enter the number of vertices: "))
g = Graph(n)

e = int(input("Enter the number of edges: "))
for _ in range(e):
    u, v = map(int, input("Enter edge (u v): ").split())
    g.addEdge(u, v)

src = int(input("Enter the source node: "))
target = int(input("Enter the target node: "))
maxDepth = int(input("Enter the maximum depth: "))

# Perform IDDFS and check if the target is reachable from the source within the max depth
result, path = g.IDDFS(src, target, maxDepth)

if result:
    print(f"Target {target} is reachable from source {src} within max depth {maxDepth}.")
    print("Traversal Path:", " -> ".join(map(str, path)))
else:
    print(f"Target {target} is NOT reachable from source {src} within max depth {maxDepth}.")
