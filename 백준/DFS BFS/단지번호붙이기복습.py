from collections import deque
n = int(input())

board = []

for _ in range(n):
    board.append(list(map(int, input())))
print(board)


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(graph, x, y):
    n = len(graph)
    queue = deque()
    queue.append((x, y))
    graph[x][y] = 0
    count = 1
    
    # 큐가 빌때까지 반복
    while queue:
        x, y = queue.popleft()
        #현재 위치에서 네방향으로 위치확인
        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y
            #공간을 벗어난 경우 체크 
            if nx < 0 or ny < 0 or nx >= n or ny >= n:
                continue
            #해당 노드를 처음 방문하는 경우에만 기록
            if graph[nx][ny] == 1:
                #왜 ? 
                graph[nx][ny] = 0
                graph.append((nx, ny))
                count += 1
    return count

cnt = []
for i in range(n):
    for j in range(n):
        if board[i][j] == 1:
            cnt.append(bfs(board, i, j))
cnt.sort()
for i in cnt:
    print(i)