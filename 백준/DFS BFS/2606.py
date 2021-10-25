N = int(input()) # 노드 수
M = int(input()) # 간선 수

graph = [[] for _ in range(N + 1)]
for i in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)


result = 0

def dfs(graph, v, visited):
    visited[v] = True
    global result
    for i in graph[v]:
        if not visited[i]:
            result += 1
            dfs(graph, i, visited)

visited = [False] * (N + 1)
dfs(graph, 1, visited)
print(result)