def rotation_90(graph, N):
    graph_90 = [[0] * N for _ in range(N)]
    for r in range(N):
        for c in range(N):
            graph_90[c][N - 1 - r] = graph[r][c]
    return graph_90


def rotation_180(graph, N):
    graph_180 = [[0] * N for _ in range(N)]
    for r in range(N):
        for c in range(N):
            graph_180[N - 1 - r][N - 1 - c] = graph[r][c]
    return graph_180


def rotation_270(graph, N):
    graph_270 = [[0] * N for _ in range(N)]
    for r in range(N):
        for c in range(N):
            graph_270[N - 1 - c][r] = graph[r][c]
    return graph_270


T = int(input())
for t in range(1, T + 1):
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]
    graph_90 = rotation_90(board, N)
    graph_180 = rotation_180(board, N)
    graph_270 = rotation_270(board, N)
    print(f"#{t}")
    for i in range(N):
        for j in range(N):
            print(graph_90[i][j], end='')
        print(end=" ")
        for k in range(N):
            print(graph_180[i][k], end='')
        print(end=" ")
        for z in range(N):
            print(graph_270[i][z], end='')
        print()