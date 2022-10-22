# 메모리 초과 recursive error
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

def dfs(v):
    for i in graph[v]:
        if parent[i] == 0:
            parent[i] = v
            dfs(i)

N = int(input())
graph = [[] for _ in range(N + 1)]
parent = [0 for _ in range(N + 1)]

for _ in range(N - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

dfs(1)

for i in parent[2:]:
    print(i)
