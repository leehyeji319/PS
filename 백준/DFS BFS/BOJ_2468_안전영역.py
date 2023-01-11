import copy
from collections import deque

N = int(input())

graph = []
min_v = int(1e9)
max_v = -1
for _ in range(N):
    l = list(map(int, input().split()))
    min_v = min(min(l), min_v)
    max_v = max(max(l), max_v)

results = []

# 빗물 채우기
def fill_rain(graph, standard):
    for i in range(N):
        for j in range(N):
            if graph[i][j] <= standard:
                graph[i][j] = 0
    return graph

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def bfs(s_r, s_c, num):
    q = deque()
    q.append((s_r, s_c))
    visited[s_r][s_c] = 1

    while q:
        r, c = q.popleft()

        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]

            if 0 <= nr < N and 0 <= nc < N and visited[nr][nc] == 0 and graph[nr][nc] > num:
                visited[nr][nc] = 1
                q.append((nr, nc))


for i in range(min_v, max_v):
    visited = [[0] * N for _ in range(N)]
    count = 0
    for j in range(N):
        for k in range(N):
            if graph[j][k] == 0:
                count = bfs(j, k)


