#d3
T = 10
for t in range(1, T + 1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]

    m = 0

    width = 0
    length = 0
    right_diagonal = 0
    left_diagonal = 0
    for i in range(100):
        right_diagonal += arr[i][i]
        left_diagonal += arr[i][99 - i]
        for j in range(100):
            width += arr[i][j]
            length += arr[j][i]

        m = max(m, width, length, right_diagonal, left_diagonal)
        width = 0
        length = 0
    print(f"#{t} {m}")