from collections import deque


def main():
    n = int(input())

    adj_matrix = []
    for _ in range(n):
        row = list(map(int, input().split()))
        adj_matrix.append(row)

    start, end = map(int, input().split())

    graph = [[] for _ in range(n + 1)]

    for i in range(n):
        for j in range(n):
            if adj_matrix[i][j] == 1:
                graph[i + 1].append(j + 1)

    if start == end:
        print(0)
        return

    path = bfs_path(graph, start, end)

    if not path or path[0] != start:
        print(-1)
    else:
        print(len(path) - 1)
        print(' '.join(map(str, path)))


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

        if current == finish:
            break

        for vertex in graph[current]:
            if not visited[vertex]:
                visited[vertex] = True
                queue.append(vertex)
                distances[vertex] = distances[current] + 1
                path[vertex] = current

    if not visited[finish]:
        return []

    result_path = []
    current = finish

    while current != -1:
        result_path.append(current)
        current = path[current]

    return result_path[::-1]


if __name__ == "__main__":
    main()