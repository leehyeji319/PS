# https://www.acmicpc.net/problem/2146

import sys
from collections import deque

sys.setrecursionlimit(10 ** 6)

input = sys.stdin.readline

N = int(input())

map = [list(map(int, input().split())) for _ in range(N)]

dr = [0, 0, 1, -1]
dc = [-1, 1, 0, 0]

ans = sys.maxsize


# 섬인애들 구하기
def island_dfs(r, c):
    global cnt
    if r <= -1 or r >= N or c <= -1 or c >= N:
        return False
    if map[r][c] == 1:
        map[r][c] = cnt
        # 상하좌우
        island_dfs(r - 1, c)
        island_dfs(r, c - 1)
        island_dfs(r + 1, c)
        island_dfs(r, c + 1)
        return True


def bridge_bfs(n):  # n은 각각 붙여준 섬의 숫자
    global ans
    visited = [[-1] * N for _ in range(N)]
    q = deque()

    for i in range(N):
        for j in range(N):
            if map[i][j] == n:
                q.append((i, j))
                visited[i][j] = 0  # 방문처리해주기

    while q:
        r, c = q.popleft()
        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]
            if nr < 0 or nr >= N or nc < 0 or nc >= N:
                continue
            # 다른섬에 도착한 경우
            if map[nr][nc] > 0 and map[nr][nc] != n:  # 다른섬에 도착햇으면 n이 다를테니까
                ans = min(ans, visited[r][c])
                return
            # 바다이고, 방문한 적이 없으면
            if map[nr][nc] == 0 and visited[nr][nc] == -1:
                visited[nr][nc] = visited[r][c] + 1
                q.append((nr, nc))


cnt = 2
for i in range(N):
    for j in range(N):
        if island_dfs(i, j):
            cnt += 1

for i in range(2, cnt):
    bridge_bfs(i)

print(ans)
