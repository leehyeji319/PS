#bfs, dfs이지만, 벽을 모두 세워서 안전 공간의 제일 최댓값을 구해야하므로 브루트포스
n, m = map(int, input().split())

#벽을 설치한 뒤의 맵 리스트
temp = [[0] * m for _ in range(n)]

data = []
for _ in range(n):
    data.append(list(map(int, input().split())))
    
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

result = 0

def virus(x, y):
    for i in range(4):
        nx = dx[i] + x
        ny = dy[i] + y
        #상하좌우 중에서 바이러스가 퍼질수있는경우
        if nx >= 0 and nx < n and ny >= 0 and ny < m:
            if temp[nx][ny] == 0:
                #해당 위치에 바이러스 심기, 다시 재귀 수행
                temp[nx][ny] = 2
                virus(nx, ny)

#안전 영역을 계산하는 메서드
def safe_zone():
    safe = 0
    for i in range(n):
        for j in range(m):
            if temp[i][j] == 0:
                safe += 1
    return safe

#깊이우선탐색으로 울타리를 설치하면서, 매번 안전영역 크기를 계산한다.
def dfs(count):
    global result
    #울타리 3개 설치된 경우
    if count == 3:
        for i in range(n):
            for j in range(m):
                temp[i][j] = data[i][j]
        #각 바이러스의 위치에서 전파진행
        for i in range(n):
            for j in range(m):
                if temp[i][j] == 2:
                    virus(i, j)
        
        #안전영역 최대값 계산
        result = max(result, safe_zone())
        return
    
    #빈 공간에 울타리 설치 
    for i in range(n):
        for j in range(m):
            if data[i][j] == 0:
                data[i][j] = 1
                count += 1
                dfs(count)
                data[i][j] = 0
                count -= 1
dfs(0)
print(result)