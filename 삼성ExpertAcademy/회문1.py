T = 10


def check_palindrome(graph, N):
    cnt = 0
    for i in range(8):
        for j in range(8 - N + 1):
            compare_arr = graph[i][j:j + N]
            if compare_arr == compare_arr[::-1]:
                cnt += 1
    return cnt


def rotation_90(graph):
    graph_90 = [[0] * 8 for _ in range(8)]
    for r in range(8):
        for c in range(8):
            graph_90[c][7 - r] = graph[r][c]
    return graph_90


for t in range(1, T + 1):
    N = int(input())
    board = [list(input()) for _ in range(8)]
    if N == 1:
        print(f"#{t} {64}")
        continue
    else:
        answer = check_palindrome(board, N) + check_palindrome(rotation_90(board), N)

    print(f"#{t} {answer}")
