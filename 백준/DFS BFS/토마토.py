from collections import deque
import queue
m, n = map(int, input().split())
board = []
for _ in range(n):
    board.append(list(map(int, input().split())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
result = 0

queue = deque()

for i in range(n):
    for j in range(m):
        if board[i][j] == 1:
            queue.append((i, j))

def bfs():
    while queue:
        x, y = queue.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < n and 0 <= ny < m and board[nx][ny] == 0:
                board[nx][ny] = board[x][y] + 1
                queue.append((nx, ny))
                
bfs()
for i in board:
    for j in i:
        if j == 0:
            print(-1)
            exit()
    result = max(result, max(i))
print(result - 1)