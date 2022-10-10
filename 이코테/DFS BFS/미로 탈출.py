from collections import deque

n, m = map(int, input().split())

board = []
for i in range(n):
    board.append(list(map(int, input())))

#이동할 네 방향 
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

#bfs 
def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    
    while queue:
        x, y = queue.popleft()
        #현재 위치에서 네 방향으로 위치 확인
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            #공간을 벗어날 경우 
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            #벽인 경우 무시
            if board[nx][ny] == 0:
                continue
            #해당 노드 처음 방문할때만 최단 거리 기록
            if board[nx][ny] == 1:
                board[nx][ny] = board[x][y] + 1
                queue.append((nx, ny))
    
    #가장 오른쪽 아래까지의 최단 거리 반환
    return board[n - 1][m - 1]

print(bfs(0,0))