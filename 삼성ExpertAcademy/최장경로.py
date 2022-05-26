T = int(input())
for t in range(1, T + 1):
    N, M = map(int, input().split())
    graph = [[] for _ in range(N + 1)]
    for i in range(M):
        a, b = map(int, input().split())
        graph[a].append(b)
    print(graph)
