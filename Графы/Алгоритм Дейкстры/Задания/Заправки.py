import heapq

#next_city - тоже самое что и neighbour из шаблона

n = int(input())
price = [0] + list(map(int, input().split()))
m = int(input())

graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

INF = float('inf')
dist = [[INF] * (n + 1) for _ in range(n + 1)]
dist[1][0] = 0
queue = [(0, 1, 0)]

while queue:
    cost, city, fuel = heapq.heappop(queue)

    if cost > dist[city][fuel]:
        continue

    if fuel < n and cost + price[city] < dist[city][fuel + 1]:
        dist[city][fuel + 1] = cost + price[city]
        heapq.heappush(queue, (cost + price[city], city, fuel + 1))

    if fuel > 0:
        for next_city in graph[city]:
            if cost < dist[next_city][fuel - 1]:
                dist[next_city][fuel - 1] = cost
                heapq.heappush(queue, (cost, next_city, fuel - 1))

result = min(dist[n])
print(result if result != INF else -1)