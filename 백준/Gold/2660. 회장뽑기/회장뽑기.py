#플로이드 와샬
import sys

input = sys.stdin.readline

N = int(input())
INF = int(1e9)

graph = [[INF] * (N + 1) for _ in range(N + 1)]
# print(graph)

while True:
    a, b = map(int, input().split())

    if a == -1 and b == -1:
        break
    graph[a][b] = 1
    graph[b][a] = 1

for i in range(1, N + 1):
    graph[i][i] = 0

for k in range(1, N + 1):  # 거치는 점
    for i in range(1, N + 1):  # 시작점
        for j in range(1, N + 1):  # 도착점
            if graph[i][j] > graph[i][k] + graph[k][j]:  # k거쳐서가는게 더 가까우면
                graph[i][j] = graph[i][k] + graph[k][j]

result = []
for i in range(1, N + 1):
    result.append(max(graph[i][1:]))

mi = min(result)
print(mi, result.count(mi))
for i, v in enumerate(result):
    if v == mi:
        print(i + 1, end=' ')