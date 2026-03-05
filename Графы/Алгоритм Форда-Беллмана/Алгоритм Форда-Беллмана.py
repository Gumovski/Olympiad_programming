from mercantile import neighbors


def bellman_ford(graph, start):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    # Релаксация рёбер
    for _ in range(len(graph)):
        change = False
        for node in graph:
            for vertex, weight in graph[node]:
                if distances[node] + weight < distances[vertex]:
                    distances[vertex] = distances[node] + weight
                    change = True
        if not change:
            break
    # Поиск отрицательных циклов
    for node in graph:
        for neighbor, weight in graph[node]:
            if distances[node] + weight < distances[neighbor]:
                raise Exception('Graph contains negative cycle')
    return distances

def bellman_ford_path(graph, start, finish):
    distances = {node: float('inf') for node in graph}
    parents = {node: None for node in graph}
    distances[start] = 0

    for _ in range(len(graph)):
        change = False
        for node in graph:
            for vertex, weight in graph[node]:
                if distances[node] + weight < distances[vertex]:
                    distances[vertex] = distances[node] + weight
                    parents[vertex] = node
                    change = True
        if not change:
            break

    for node in graph:
        for neighbor, weight in graph[node]:
            if distances[node] + weight < distances[neighbor]:
                raise Exception('Graph contains negative cycle')

    path = []
    current = finish
    if distances[current] == float('inf'):
        return None
    while current:
        path.append(current)
        current = parents[current]
    return path[::-1]

def bellman_ford_get_negative_cycle(graph, start):
    distances = {node: float('inf') for node in graph}
    parents = {node: None for node in graph}
    distances[start] = 0

    # n-1 проходов
    for _ in range(len(graph) - 1):
        for node in graph:
            for vertex, weight in graph[node]:
                # Добавлена проверка parents[node] != vertex
                if distances[node] != float('inf') and distances[node] + weight < distances[vertex]:
                    if parents[node] != vertex:
                        distances[vertex] = distances[node] + weight
                        parents[vertex] = node

    # n-й проход — только ищем relaxed_node, parents НЕ МЕНЯЕМ
    relaxed_node = None
    for node in graph:
        for vertex, weight in graph[node]:
            if distances[node] != float('inf') and distances[node] + weight < distances[vertex]:
                # Добавлена такая же проверка
                if parents[node] != vertex:
                    distances[vertex] = distances[node] + weight
                    relaxed_node = vertex

    if relaxed_node is None:
        return None

    # Гарантированно попадаем внутрь цикла
    current = relaxed_node
    for _ in range(len(graph)):
        current = parents[current]

    # Собираем цикл
    cycle = []
    start_cycle_node = current
    while True:
        cycle.append(current)
        current = parents[current]
        if current == start_cycle_node:
            break
    cycle.append(start_cycle_node)

    return cycle[::-1]

if __name__ == '__main__':
    graph = {
        'A': [('B', 1), ('C', -4)],
        'B': [('A', 1), ('C', 2), ('D', 5)],
        'C': [('B', 2), ('A', -4), ('D', 1)],
        'D': [('B', 5), ('C', 1)],
        'E': [('C', 1)],
    }
    print(bellman_ford_get_negative_cycle(graph, 'A'))