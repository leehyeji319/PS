import sys
from collections import deque

input = sys.stdin.readline


def bfs_general(graph, r, c, visited, color):
    q = deque()
    q.append((r, c))
    visited[r][c] = True

    while q:
        r, c = q.popleft()

        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]

            if 0 <= nr < N and 0 <= nc < N and not visited[nr][nc]:
                if color == graph[nr][nc]:
                    q.append((nr, nc))
                    visited[nr][nc] = True
    return


def bfs_color(graph, r, c, visited, color):
    q = deque()
    q.append((r, c))
    visited[r][c] = True

    while q:
        r, c = q.popleft()

        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]

            if 0 <= nr < N and 0 <= nc < N and not visited[nr][nc]:
                if (color == 'R' or color == 'G') and (graph[nr][nc] == 'R' or graph[nr][nc] == 'G'):
                    q.append((nr, nc))
                    visited[nr][nc] = True
                elif color == graph[nr][nc]:
                    q.append((nr, nc))
                    visited[nr][nc] = True

    return


N = int(input())
graph = [list(input().rstrip()) for _ in range(N)]
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
result = []

visited = [[False] * N for _ in range(N)]
# 일반인
cnt = 0
for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            bfs_general(graph, i, j, visited, graph[i][j])
            cnt += 1
result.append(cnt)

visited = [[False] * N for _ in range(N)]
cnt = 0

# 적록색약
for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            bfs_color(graph, i, j, visited, graph[i][j])
            cnt += 1
result.append(cnt)

for r in result:
    print(r, end=" ")