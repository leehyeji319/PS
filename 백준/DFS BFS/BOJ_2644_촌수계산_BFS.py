import sys
from collections import deque

input = sys.stdin.readline
N = int(input())
t1, t2 = map(int, input().split())
M = int(input())

graph = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False] * (N + 1)

ans = 0


def bfs(graph, start, visited):
    if start == t2:
        return

    global ans
    q = deque([start])
    visited[start] = True
    while q:
        v = q.popleft()

        for i in graph[v]:
            if not visited[i]:
                q.append(i)
                visited[i] = True

                ans += 1


bfs(graph, t1, visited)

print(ans)
