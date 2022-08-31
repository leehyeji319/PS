# import sys
# input = sys.stdin.readline


def cancel(row, col, d, plus): #되돌리기
    for _ in range(plus):
        graph[row + dr[d]][col + dc[d]] = 0
        row += dr[d]
        col += dc[d]
    pass


def setting(row, col, d):
    _row = row
    _col = col
    plus = 0
    while 0 <= row + dr[d] < N and 0 <= col + dc[d] < N:
        row += dr[d]
        col += dc[d]
        if graph[row][col]:
            break
        graph[row][col] = 1
        plus += 1 #전선을 놓을때마다 plus += 1
    else:
        return plus
    cancel(_row, _col, d, plus)
    return 0


def dfs(now, last, code):
    global max_cores, min_value
    if max_cores < len(now):
        max_cores = len(now)
        min_value = int(1e9)
    if max_cores == len(now) and min_value > code:
        min_value = code
    for i in range(last, len(cores)):
        for d in range(4):
            plus = setting(*cores[i], d)
            if not plus:
                continue
            next = now[:]
            next.append(i)
            dfs(next, i + 1, code + plus)

            cancel(*cores[i], d, plus)


T = int(input())

# 상하좌우
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


for tc in range(1, T + 1):
    N = int(input())
    graph = [list(map(int, input().split())) for _ in range(N)]
    fix = 0
    cores = []
    for r in range(N):
        for c in range(N):
            if graph[r][c]:
                if r == 0 or r == N - 1 or c == 0 or c == N - 1:
                    fix += 1 #이미 연결되어있는 코어 갯수 찾기
                else:
                    cores.append((r, c)) #이미 연결되어있다고 보지 않는 것들 -> 확인할 것들
    max_cores = -1
    min_value = int(1e9)
    dfs([], 0, 0)
    print(f"#{tc} {min_value}")

