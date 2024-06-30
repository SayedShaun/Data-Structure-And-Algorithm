# Graph Travarsal Algorithm

# Recursive DFS
def recursive_dfs(graph, start, visited):
    visited.add(start)
    for neighbor in graph[start]:
        if neighbor not in visited:
            recursive_dfs(graph, neighbor, visited)
    return visited

#DFS
def dfs(graph, start):
    visited = set()
    stack = [start]
    while stack:
        vertex = stack.pop()
        for neighbor in graph[vertex]:
            if neighbor not in visited:
                visited.add(neighbor)
                stack.append(neighbor)
    return visited

# BFS
def bfs(graph, start):
    visited = set()
    queue = [start]
    while queue:
        vertex = queue.pop(0)
        for neighbor in graph[vertex]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    return visited


graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

print(f"Recursive DFS: {recursive_dfs(graph, 'A', set())}")
print(f"BFS: {bfs(graph, 'A')}")
print(f"DFS: {dfs(graph, 'A')}")
