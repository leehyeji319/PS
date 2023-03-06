#https://www.acmicpc.net/problem/16967
# 크기가 H, W  정수가 X, Y
H, W, X, Y = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(H + X)]

original = [graph[i][:W] for i in range(H)]

overlap = [graph[i][Y: Y + W - 1] for i in range(X, H + X - 1)]

for i in range(H):
    for j in range(W):
        if i + X < H and j + Y < W:
            original[i + X][j + Y] -= original[i][j]

for o in original:
    print(" ".join(map(str, o)))