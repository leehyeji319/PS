import sys

input = sys.stdin.readline

N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]
visited = [False for _ in range(N)]
INF = int(1e9)
res = INF

def dfs(depth, index):
    global res
    if depth == N // 2:
        S = 0
        L = 0

        for i in range(N):
            for j in range(N):
                if visited[i] and visited[j]:
                    S += graph[i][j]
                elif not visited[i] and not visited[j]:
                    L += graph[i][j]
        res = min(res, abs(S - L))
        return

    for i in range(index, N):
        if not visited[i]:
            visited[i] = True
            dfs(depth + 1, i + 1)
            visited[i] = False

dfs(0, 0)
print(res)
