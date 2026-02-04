from collections import deque

n, m = map(int, input().split())
maze = [input() for i in range(n)]

queue = deque([(0, 0, 0)])
visited = [[False] * m for j in range(n)]
visited[0][0] = True

while queue:
    x, y, step = queue.popleft()

    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        nx, ny = x, y

        while True:
            next_x, next_y = nx + dx, ny + dy

            if not (0 <= next_x < n and 0 <= next_y < m):
                break

            if maze[next_x][next_y] == '1':
                break

            nx, ny = next_x, next_y

            if maze[nx][ny] == '2':
                print(step + 1)
                exit()

        if not visited[nx][ny]:
            visited[nx][ny] = True
            queue.append((nx, ny, step + 1))
#