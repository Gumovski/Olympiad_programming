def find_all_cycles(graph):
    visited = set()
    cycles = []
    path = []
    def dfs(_graph, current, _vertex):
        visited.add(_vertex)
        path.append(_vertex)
        for neighbor in _graph[_vertex]:
            if neighbor not in visited:
                dfs(_graph, current, neighbor)
            elif current == neighbor and len(path) > 2:
                cycles.append(path.copy())
        path.pop()
        visited.remove(_vertex)

    for vertex in graph:
        dfs(graph, vertex, vertex)
        visited.add(vertex)
    return cycles

graph = {
    'A': ['B', 'C'],
    'C': ['D', 'E'],
    'D': ['A', 'F', 'G'],
    'H': ['D', 'F'],
    'G': ['H'],
    'E': ['D'],
    'B': [],
    'F': []
}

print(find_all_cycles(graph))