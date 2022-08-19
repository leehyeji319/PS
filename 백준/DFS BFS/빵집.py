
def dfs(r, c):
    if c == C - 1: #마지막에 도착하면
        return True

    for d in dr:
        if 0 <= r + d < R and graph[r + d][c + 1] == '.' and not visited[r + d][c + 1]:
            visited[r + d][c + 1] = True
            if dfs(r + d, c + 1):
                return True
    return False

R, C = map(int, input().split())

graph = [list(input().rstrip()) for _ in range(R)]
visited = [[False] * C for _ in range(R)]
dr = [-1, 0, 1]
answer = 0

for i in range(R):
    if graph[i][0] == '.':
        if dfs(i, 0):
            answer += 1
print(answer) 