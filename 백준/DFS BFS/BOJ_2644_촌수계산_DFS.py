import sys
input = sys.stdin.readline


N = int(input()) # 노드 수
t1, t2 = map(int, input().split())
L = int(input()) # 간선 수

graph = [[] for _ in range(N + 1)]

visited = [False] * (N + 1)

for _ in range(L):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

ans = 0


def dfs(graph, v, visited):
    if v == t2:
        return

    visited[v] = True
    global ans
    for i in graph[v]:
        if not visited[i]:
            ans += 1
            dfs(graph, i, visited)

dfs(graph, t1, visited)

print(ans)