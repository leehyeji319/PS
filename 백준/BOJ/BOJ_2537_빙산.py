# 1. 0과 접해있는 갯수만큼 매해 빙산이 녹음
# 2. 빙산은 0보다 내려가지 않는다.
# 3. 빙산이 두 덩어리 이상으로 분리되는 최소 시간(년)을 구해
# 4. 만약 두덩어리 이상으로 분리되지않으면 0을 출력
from collections import deque


def count_zero(r, c):
    zero_cnt = 0
    for d in range(4):
        if graph[r - 1][c] == 0:
            zero_cnt += 1
        if graph[r + 1][c] == 0:
            zero_cnt += 1
        if graph[r][c - 1] == 0:
            zero_cnt += 1
        if graph[r][c + 1] == 0:
            zero_cnt += 1
    return zero_cnt


def bfs(r, c):
    queue = deque()
    queue.append((r, c))
    visited[r][c] = True

    while queue:
        r, c = queue.popleft()
        for d in range(4):
            nr = dr[d] + r
            nc = dc[d] + c

            if nr < 1 or nc < 1 or nr >= N or nc >= M:
                continue
            graph[nr][nc] = True
            graph.append((nr, nc))

    return 1


N, M = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(N)]

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

year_cnt = 0  # 년수
check = False


while True:
    # 탈출 조건 -> 두덩이 이상 됐거나, 모두 0이 됏거나

    year_cnt += 1

    for r in range(1, N - 1):
        for c in range(1, M - 1):
            # 4방탐색해서 빙하 녹이기
            if graph[r][c] != 0:
                zero = count_zero(r, c)
                if graph[r][c] > 0:
                    graph[r][c] -= zero
                if graph[r][c] <= 0:
                    graph[r][c] = 0

    # 방문처리 배열
    visited = [[False] * M for _ in range(N)]
    # 두덩이 이상인지 확인
    cnt = []
    for i in range(N):
        for j in range(M):
            if graph[r][c] != 0:
                cnt.append(bfs(i, j))

    if len(cnt) == 0:
        break
    if len(cnt) >= 2:
        check = True
        break

if check: print(year_cnt)
else: print(0)
