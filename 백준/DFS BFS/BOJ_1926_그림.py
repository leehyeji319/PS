import sys
from collections import deque

sys.setrecursionlimit(3000000)
input = sys.stdin.readline


def bfs(graph, x, y):
    q = deque()
    q.append((x, y))
    graph[x][y] = 0
    count = 1

    while q:
        r, c = q.popleft()

        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]

            if 0 <= nr < N and 0 <= nc < M and graph[nr][nc] == 1:
                count += 1
                graph[nr][nc] = 0
                q.append((nr, nc))

    return count


N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

cnt = []

for r in range(N):
    for c in range(M):
        if graph[r][c] == 1:
            cnt.append(bfs(graph, r, c))
cnt.sort(reverse=True)

if len(cnt) == 0:
    print(0)
    print(0)
    exit()

print(len(cnt))
print(cnt[0])
