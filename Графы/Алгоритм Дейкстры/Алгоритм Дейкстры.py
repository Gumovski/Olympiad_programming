import heapq


def dijkstra(graph, start):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    queue = [(0, start)]
    while queue:
        current_distance, current_vertex = heapq.heappop(queue)
        if current_distance > distances[current_vertex]:
            continue
        for neighbor, weight in graph[current_vertex]:
            new_distance = current_distance + weight
            if new_distance < distances[neighbor]:
                distances[neighbor] = new_distance
                heapq.heappush(queue, (new_distance, neighbor))
    return distances

def dijkstra_path(graph, start, finish):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    parents = {node: None for node in graph}
    queue = [(0, start)]
    while queue:
        current_distance, current_vertex = heapq.heappop(queue)
        if current_distance > distances[current_vertex]:
            continue
        for neighbor, weight in graph[current_vertex]:
            new_distance = current_distance + weight
            if new_distance < distances[neighbor]:
                distances[neighbor] = new_distance
                heapq.heappush(queue, (new_distance, neighbor))
                parents[neighbor] = current_vertex
    path = []
    current = finish
    while current:
        path.append(current)
        if current == start:
            break
        current = parents[current]
    if path[-1] != start:
        return None
    return path[::-1]


if __name__ == '__main__':
    graph = {
        'A': [('B', 1), ('C', 4)],
        'B': [('A', 1), ('C', 2), ('D', 5)],
        'C': [('B', 2), ('A', 4), ('D', 1)],
        'D': [('B', 5), ('C', 1)],
        'E': [('C', 1)],
    }
    print(dijkstra_path(graph, 'D', 'E'))