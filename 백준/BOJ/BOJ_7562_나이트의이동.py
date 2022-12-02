import sys
from collections import deque

input = sys.stdin.readline

T = int(input())

dr = [-2, -2, -1, -1, 1, 1, 2, 2]
dc = [-1, 1, -2, 2, -2, 2, -1, 1]

for tc in range(1, T + 1):
    L = int(input())
    graph = [[0] * int(L) for _ in range(L)]
    start_r, start_c = map(int, input().split())
    end_r, end_c = map(int, input().split())
    visited = [[0] * L for _ in range(L)]

    def bfs():
        q = deque()
        q.append((start_r, start_c))

        while q:
            r, c = q.popleft()

            if r == end_r and c == end_c:
                print(graph[r][c])
                return

            for d in range(8):
                nr = r + dr[d]
                nc = c + dc[d]

                if nr >= L or nc >= L or nr < 0 or nc < 0 or visited[nr][nc] != 0:
                    continue

                visited[nr][nc] = 1
                q.append((nr, nc))
                graph[nr][nc] = graph[r][c] + 1

                # if nr == end_r and nc == end_c:
                #     print(graph[nr][nc])
                #     return
    bfs()
