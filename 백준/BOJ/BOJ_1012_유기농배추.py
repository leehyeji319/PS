import sys
from collections import deque

input = sys.stdin.readline

T = int(input())

for t in range(1, T + 1):

    M, N, K = map(int, input().split())
    graph = [[0] * M for _ in range(N)]

    for _ in range(K):
        a, b = map(int, input().split())
        graph[b][a] = 1

    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]


    def bfs(s_r, s_c):
        q = deque()
        q.append((s_r, s_c))
        graph[s_r][s_c] = 0
        while q:
            r, c = q.popleft()

            for d in range(4):
                nr = r + dr[d]
                nc = c + dc[d]

                if nr >= N or nc >= M or nr < 0 or nc < 0:
                    continue

                if graph[nr][nc] == 1:
                    graph[nr][nc] = 0
                    q.append((nr, nc))
        return True


    cnt = 0

    for i in range(N):
        for j in range(M):
            if graph[i][j] == 1:
                if bfs(i, j):
                    cnt += 1

    print(cnt)
