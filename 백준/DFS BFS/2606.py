N = int(input()) # 노드 수
M = int(input()) # 간선 수

board = [[] for _ in range(N + 1)]
for i in range(M):
    a, b = map(int, input().split())
    board[a].append(b)
    board[b].append(a)


result = 0

def dfs(graph, v, visited):
    visited[v] = True
    global result
    for i in graph[v]:
        if not visited[i]:
            result += 1
            dfs(graph, i, visited)

visited = [False] * (N + 1)
dfs(board, 1, visited)
print(result)