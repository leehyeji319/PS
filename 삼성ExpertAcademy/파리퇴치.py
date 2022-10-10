T = int(input())

for t in range(1, T + 1):
    N, M = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]
    fly = 0
    for i in range(N - M + 1):
        for j in range(N - M + 1):
            tmp = 0
            for a in range(i, i + M):
                for b in range(j, j + M):
                    tmp += board[a][b]
            if tmp > fly:
                fly = tmp
    print(f"#{t} {fly}")
