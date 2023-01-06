import sys
from collections import deque

input = sys.stdin.readline

M, N, K = map(int, input().split()) # M = 5, N = 7

graph = [[False] * N for _ in range(M)]
areas = []

for i in range(1, K + 1):
    l_x, l_y, r_x, r_y = map(int, input().split()) # 0 2 4 4
    height = r_y - l_y
    width = r_x - l_x

    for j in range(l_y, l_y + height):
        for k in range(l_x, l_x + width):
            if not graph[j][k]:
                graph[j][k] = True

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def bfs(graph, x, y):
    q = deque()
    q.append((x, y))
    graph[x][y] = True
    count = 1

    while q:
        r, c = q.popleft()

        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]

            if 0 <= nr < M and 0 <= nc < N and not graph[nr][nc]:
                count += 1
                graph[nr][nc] = True
                q.append((nr, nc))

    return count


for i in range(M):
    for j in range(N):
        if not graph[i][j]:
            areas.append(bfs(graph, i, j))

areas.sort()

print(len(areas))
for i in areas:
    print(i, end = " ")