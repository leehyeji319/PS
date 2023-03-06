# https://www.acmicpc.net/problem/17484
N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]


def dfs(r, c, fuel, dir):
    global answer
    if r == N - 1:  # 달에 도착하면
        if fuel < answer:
            answer = fuel
            return

    for d in range(3):
        nr = dr[d] + r
        nc = dc[d] + c
        if dir != d and 0 <= nr < N and 0 <= nc < M:
            dfs(nr, nc, fuel + board[nr][nc], d)


dr = [1, 1, 1]
dc = [-1, 0, 1]

# 1. 대각선 왼쪽 아래, 아래, 대각선 오른쪽 아래
# 2. 같은 방향으로 두번 연속으로 움직일 수 없다.
# 3. 연료를 최대한 아껴야함 연료의 최소값 계산

visited = [[False] * M for _ in range(N)]
answer = int(1e9)

for i in range(M):
    dfs(0, i, board[0][i], 3)

print(answer)