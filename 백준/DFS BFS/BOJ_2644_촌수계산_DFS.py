import sys

input = sys.stdin.readline

N = int(input())  # 노드 수
t1, t2 = map(int, input().split())
L = int(input())  # 간선 수

graph = [[] for _ in range(N + 1)]

visited = [False] * (N + 1)
result = []
for _ in range(L):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)


def dfs(v, ans):
    ans += 1
    if v == t2:
        result.append(ans)
        return

    visited[v] = True

    for i in graph[v]:
        if not visited[i]:
            dfs(i, ans)


dfs(t1, 0)

if len(result) == 0:
    print(-1)
else:
    print(result[0] - 1)
