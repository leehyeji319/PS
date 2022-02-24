import sys
sys.setrecursionlimit(10000)
t = int(input())

def dfs(x, y):
    if x <= -1 or x >= m or y <= -1 or y >= n:
        return 0
    if graph[x][y] == 1:
        graph[x][y] = 0
        dfs(x - 1, y)
        dfs(x, y - 1)
        dfs(x + 1, y)
        dfs(x, y + 1)
        return 1
    return 0

for _ in range(t):
    m, n, k = map(int, input().split())
    graph = [[0] * n for _ in range(m)]
    for i in range(k):
        x, y = map(int, input().split())
        graph[x][y] = 1
        
    result = 0
    for j in range(m):
        for r in range(n):
            if dfs(j, r) == 1:
                result += 1
    print(result)




    