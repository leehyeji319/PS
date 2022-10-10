INF = int(1e9)

n = int(input()) # 노드
m = int(input()) # 간선

board = [[INF] * (n + 1) for _ in range(n + 1)]

for a in range(1, n + 1):
    for b in range(1, n + 1):
        if a == b:
            board[a][b] = 0

#간선 정보 입력받기
for _ in range(m):
    a, b, c = map(int, input().split())
    if board[a][b] > c:
        board[a][b] = c

for k in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            board[a][b] = min(board[a][b], board[a][k] + board[k][b])

for a in range(1, n + 1):
    for b in range(1, n + 1):
        if board[a][b] == INF:
            print(0, end=" ")
        else:
            print(board[a][b], end=" ")
    print()