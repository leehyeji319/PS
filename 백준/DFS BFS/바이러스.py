n = int(input()) #노드수
m = int(input()) #간선수

graph = [[] for _ in range(n + 1)] #2차원 배열

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

result = 0

def dfs(graph, v, visited):
    #현재 노드 방문 처리 
    visited[v] = True
    global result
    for i in graph[v]:
        if not visited[i]:
            result += 1
            dfs(graph, i, visited)
visited = [False] * (n + 1)
dfs(graph, 1, visited)
print(result)