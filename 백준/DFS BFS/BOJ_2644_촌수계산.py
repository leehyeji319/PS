import sys
input = sys.stdin.readline

def dfs(graph, v, visited):
    global ans

    if v == t2:
        return

    visited[v] = True

    for i in graph[v]:
        if not visited[i]:
            ans += 1
            dfs(graph, i, visited)


N = int(input())
t1, t2 = map(int, input().split())
L = int(input()) # 간선 수

graph = [[] for _ in range(N + 1)]

visited = [False] * (N + 1)

for _ in range(L):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

ans = 0


dfs(graph, t1, visited)

if ans == 0:
    print(-1)
else: print(ans)