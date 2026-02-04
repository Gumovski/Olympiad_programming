
# DFS - depth first search
def dfs(graph, vertex):
    visited = set()
    def dfs_recursive(graph, vertex, visited):
        visited.add(vertex)
        for neighbor in graph[vertex]:
            if neighbor not in visited:
                dfs_recursive(graph, neighbor, visited)
    return dfs_recursive(graph, vertex, visited)


