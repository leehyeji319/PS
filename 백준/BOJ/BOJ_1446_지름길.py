import sys
import heapq

input = sys.stdin.readline
INF = int(1e9)
N, D = map(int, input().split())

graph = [[] for _ in range(D + 1)]
distance = [INF] * (D + 1)

for i in range(D):
    graph[i].append((i + 1, 1))

for _ in range(N):
    f, t, c = map(int, input().split())
    if t > D or (t - f) <= c:
        continue
    graph[f].append((t, c))

start, end = 0, D


def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)

        if distance[now] < dist:
            continue

        for i in graph[now]:
            cost = dist + i[1]

            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))


dijkstra(start)
print(distance[end])
