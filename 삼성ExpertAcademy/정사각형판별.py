T = int(input())


def check_square(board, cnt, N):
    for i in range(N):
        for j in range(N):
            if board[i][j] == 1:
                down = 0
                right = 0

                for k in range(i + 1, N):
                    if board[k][j] == 1:
                        down += 1
                    else:
                        break

                for k in range(j + 1, N):
                    if board[i][k] == 1:
                        right += 1
                    else:
                        break

                if down is not right:
                    return 'no'

                for x in range(i, i + down + 1):
                    for y in range(j, j + right + 1):
                        if board[x][y] == 1:
                            cnt -= 1
                        else:
                            return 'no'
                if cnt != 0:
                    return 'no'
                return 'yes'


for t in range(1, T + 1):
    N = int(input())
    graph = [list(input()) for _ in range(N)]
    # 0으로 채운 배열 선언
    board = [[0] * N for _ in range(N)]
    cnt = 0
    for i in range(N):
        for j in range(N):
            if graph[i][j] == '#':
                board[i][j] = 1
                cnt += 1
            else:
                continue
    result = check_square(board, cnt, N)
    print(f"#{t} {result}")