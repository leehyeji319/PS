import sys
from collections import deque


def printGraph(graph):
    for g in graph:
        print(g)
    print("=================")
    print()


input = sys.stdin.readline

N, M = map(int, input().split())
graph = [list(map(int, input().strip())) for _ in range(N)]

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def bfs(s_r, s_c):
    q = deque()
    q.append((s_r, s_c))

    while q:
        r, c = q.popleft()
        # printGraph(graph)
        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]

            if nr >= N or nc >= M or nr < 0 or nc < 0 or graph[nr][nc] == 0:
                continue

            if graph[nr][nc] == 1:
                graph[nr][nc] = graph[r][c] + 1
                q.append((nr, nc))

    return graph[N - 1][M - 1]


print(bfs(0, 0))
