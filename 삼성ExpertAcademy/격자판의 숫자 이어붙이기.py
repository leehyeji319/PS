# 중복순열, 범위체크,

def dfs(idx, row, col, num):
    global dr
    global dc
    num += board[row][col]
    if idx == 6:
        result.append(num)
        return
    for i in range(4):
        nr = row + dr[i]
        nc = col + dc[i]
        if 0<= nr < 4 and 0<= nc < 4:
            dfs(idx+1, nr, nc, num)

T = int(input())
for tc in range(1, T + 1):

    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    board = [list(map(str, input().split())) for _ in range(4)]
    result = []
    for r in range(4):
        for c in range(4):
            dfs(0, r, c, "")

    answer = set(result)
    print(f"#{tc} {len(answer)}")



