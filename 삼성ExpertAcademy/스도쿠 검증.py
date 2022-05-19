T = int(input())
for t in range(1, T + 1):
    sdoku = [list(map(int, input().split())) for _ in range(9)]
    for x in range(9):
        for y in range(9):
            print(sdoku[x][y], end='')
            print(sdoku[y][x], end='')