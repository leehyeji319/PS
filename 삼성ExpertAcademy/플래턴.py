T = 10
for t in range(1, T + 1):
    dump = int(input())
    board = list(map(int, input().split()))
    while dump > 0:
        board.sort(reverse=True)
        board[0] -= 1
        board[-1] += 1
        dump -= 1
        if (max(board) - min(board)) <= 1:
            break
    answer = max(board) - min(board)

    print(f"#{t} {answer}")
