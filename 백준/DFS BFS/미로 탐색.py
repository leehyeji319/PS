from collections import deque

n, m = map(int, input().split())

board = []
for _ in range(n):
    board.append(list(map(int, input())))
    
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    
    while queue:
        x, y = queue.popleft()
        
        for i in range(4):
            # 현재 위치에서 네방향으로 위치 확인
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            #벽이면 무시
            if board[nx][ny] == 0:
                continue
            
            if board[nx][ny] == 1:
                board[nx][ny] = board[x][y] + 1
                queue.append((nx, ny))
    
    #최단거리 반환
    return board[n - 1][m - 1]

print(bfs(0,0))