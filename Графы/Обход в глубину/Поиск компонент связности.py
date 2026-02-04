def find_connected_components(graph: dict):
    visited = set()
    components = []
    for vertex in graph.keys():
        if vertex not in visited:
            component = []
            def dfs(_graph, _vertex, _visited, _component):
                _visited.add(_vertex)
                _component.append(_vertex)
                for neighbor in _graph[_vertex]:
                    if neighbor not in _visited:
                        dfs(_graph, neighbor, _visited, _component)
            dfs(graph, vertex, visited, component)
            components.append(component)
    return components

graph = {
    'A': ['B'],
    'B': ['A', 'C'],
    'C': ['B', 'D'],
    'D': ['C'],
    'E': [],
    'F': ['G'],
    'G': ['F'],
}
print(find_connected_components(graph))