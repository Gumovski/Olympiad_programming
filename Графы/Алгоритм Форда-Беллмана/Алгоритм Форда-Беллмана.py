def bellman_ford(graph, start):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    # Релаксация рёбер
    for _ in range(len(graph)):
        for node in graph:
            for vertex, weight in graph[node]:
                if distances[node] + weight < distances[vertex]:
                    distances[vertex] = distances[node] + weight
    # Поиск отрицательных циклов
    for node in graph:
        for neighbor, weight in graph[node]:
            if distances[node] + weight < distances[neighbor]:
                raise Exception('Graph contains negative cycle')
    return distances

# TODO: С восстановлением пути

# TODO: С восстановлением пути отрицательного цикла

if __name__ == '__main__':
    graph = {
        'A': [('B', 1), ('C', 4)],
        'B': [('A', 1), ('C', 2), ('D', 5)],
        'C': [('B', 2), ('A', 4), ('D', 1)],
        'D': [('B', 5), ('C', 1)],
        'E': [('C', 1)],
    }
