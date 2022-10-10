from collections import deque

m, n, h = map(int, input().split())

board = [[list(map(int, input().split())) for _ in range(n)] for _ in range(h)]

dx = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, -1, 1, 0, 0]
dz = [0, 0, 0, 0, -1, 1]

queue = deque()

def bfs():
    while queue:
        z, x, y = queue.popleft()

        for i in range(6):
            nx = dx[i] + x
            ny = dy[i] + y
            nz = dz[i] + z
            
            if 0 <= nx < n and 0 <= ny < m and 0 <= nz < h:
                #높이,x,y 순서
                if board[nz][nx][ny] == 0:
                    board[nz][nx][ny] = board[z][x][y] + 1
                    queue.append([nz, nx, ny])

for i in range(h):
    for j in range(n):
        for k in range(m):
            if board[i][j][k] == 1:
                queue.append((i, j, k))

bfs()
flag = 0
result = -2

for i in range(h):
    for j in range(n):
        for k in range(m):
            if board[i][j][k] == 0:
                flag = 1
            result = max(result, board[i][j][k])
            
if flag == 1:
    print(-1)
elif result == -1:
    print(0)
else: print(result - 1)

#이거 무조건 복습하기 ;;