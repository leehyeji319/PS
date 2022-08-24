
N, M, X, Y, K = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
command = list(map(int, input().split()))
dic = {1: (0, 1), 2: (0, -1), 3: (-1, 0), 4: (1, 0)}
dice_num = [0] * 6
dice_idx = [1, 2, 3, 4, 5, 6]