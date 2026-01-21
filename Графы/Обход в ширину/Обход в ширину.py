from collections import deque

# bfs - breadth first search
def bfs(graph, start):
    queue = deque([start])
    visited = [False] * len(graph)
    distances = [-1] * len(graph)

    distances[start] = 0
    visited[start] = True
    while queue:
        current = queue.popleft()

        for vertex in graph[current]:
            if not visited[vertex]:
                visited[vertex] = True
                queue.append(vertex)
                distances[vertex] = distances[current] + 1
    return distances

def bfs_path(graph, start, finish):
    size = len(graph)
    queue = deque([start])
    visited = [False] * size
    distances = [-1] * size
    path = [-1] * size

    distances[start] = 0
    visited[start] = True
    while queue:
        current = queue.popleft()

        for vertex in graph[current]:
            if not visited[vertex]:
                visited[vertex] = True
                queue.append(vertex)
                distances[vertex] = distances[current] + 1
                path[vertex] = current

    result_path = []
    current = finish
    while current:
        result_path.append(current)
        current = path[current]

    return result_path[::-1]

