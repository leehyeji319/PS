import sys

input = sys.stdin.readline


# 낚시왕이 낚시를 한다
def fishing(j):
    for i in range(R):
        if board[i][j]:
            x = board[i][j][2]
            board[i][j] = 0
            return x
    return 0


# 일초 돌고나서 상어쉑위치
def shark_next_location(r, c, speed, dir):
    nr = r
    nc = c
    while speed > 0:
        nr += direction[dir][0]
        nc += direction[dir][1]
        if nr < 0 or nr >= R or nc < 0 or nc >= C:
            if dir % 2 == 0:
                dir -= 1
            else:
                dir += 1
            nr += direction[dir][0] * 2
            nc += direction[dir][1] * 2
        speed -= 1
    return nr, nc, dir


# 상어들이 일초마다 움직
def move():
    global board
    new_graph = [[0 for _ in range(C)] for _ in range(R)]
    for r in range(R):
        for c in range(C):
            if board[r][c]:
                # print(graph[r][c][0], graph[r][c][1])
                nr, nc, nd = shark_next_location(r, c, board[r][c][0], board[r][c][1])  # 얘가 없는애가 잇네 ..
                if new_graph[nr][nc]:
                    new_graph[nr][nc] = max(
                        new_graph[nr][nc],
                        (board[r][c][0], nd, board[r][c][2]),
                        key=lambda x: x[2]
                    )
                else:
                    new_graph[nr][nc] = (board[r][c][0], nd, board[r][c][2])
    board = new_graph


R, C, M = map(int, input().split())
board = [[0 for _ in range(C)] for _ in range(R)]

for _ in range(M):
    r, c, s, d, z = map(int, input().split())
    board[r - 1][c - 1] = (s, d, z)
# print(board)
direction = {1: (-1, 0), 2: (1, 0), 3: (0, 1), 4: (0, -1)}  # 상하우좌

ans = 0
for j in range(C):
    ans += fishing(j)
    move()

print(ans)
