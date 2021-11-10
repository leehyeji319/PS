# 7562 나이트의 이동
from collections import deque
t = int(input())

for _ in range(t):
    i = int(input())
    row, column = map(int, input().split())
    now_location = [row, column]

    next_row, next_column = map(int, input().split())
    next_location = [next_row, next_column]

    visitied = [[0] * i for _ in range(i)]
    visitied[row][column] = 1

    # 나이트가 이동할 수 있는 경우의 수
    steps = [(-2, -1), (-2, 1), (2, -1), (2, 1), (-1, 2), (1, 2), (-1, -2), (1, -2)]

    queue = deque()
    queue.append((row, column, 0))

    while queue:
        temp = queue.popleft()
        row, column = temp[0], temp[1]
        
        if row == next_row and column == next_column:
            print(temp[2])
            break
        
        for step in steps:
        # 이동하고자 하는 위치
            new_row = row + step[0]
            new_column = column + step[1]
            if 0 <= new_row and new_row < i and 0 <= new_column and new_column < i and visitied[new_row][new_column] == 0:
                visitied[new_row][new_column] = 1
                queue.append((new_row, new_column, temp[2] + 1))