T = int(input())

for t in range(1, T + 1):
    n, m = map(int, input().split())
    graph = [[0] * n for _ in range(n)]
    b_cnt, w_cnt = 0, 0

    graph[n // 2 - 1][n // 2 - 1] = 2
    graph[n // 2 - 1][n // 2] = 1
    graph[n // 2][n // 2 - 1] = 1
    graph[n // 2][n // 2] = 2

    dx = [-1, 1, 0, 0, 1, 1, -1, -1]
    dy = [0, 0, -1, 1, 1, -1, 1, -1]

    for _ in range(m):
        x, y, c = map(int, input().split())
        x -= 1
        y -= 1
        graph[x][y] = c
        for i in range(8):
            nx = x
            ny = y
            reverse = []
            while True:
                nx += dx[i]
                ny += dy[i]

                if nx < 0 or ny < 0 or nx >= n or ny >= n:
                    reverse = []
                    break
                elif graph[nx][ny] == 0:
                    reverse = []
                    break
                elif graph[nx][ny] == c:
                    break
                else:
                    reverse.append((nx, ny))

            for rx, ry in reverse:
                graph[rx][ry] = c

    for g in graph:
        b_cnt += g.count(1)
        w_cnt += g.count(2)

    print(f"#{t} {b_cnt} {w_cnt}")
