def dfs(graph, v, cnt):
    if cnt == 4:
        print(1)
        exit()
    for i in graph[v]:
        if not visited[i]:
            visited[i] = True
            dfs(graph, i, cnt + 1)
            visited[i] = False


n, m = map(int, input().split())
graph = [[] for _ in range(n)]

for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False] * n
cnt = 0

for v in range(n):
    visited[v] = True
    dfs(graph, v, cnt)
    visited[v] = False

print(0)