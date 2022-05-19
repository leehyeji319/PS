import sys

N, M = map(int, input().split())
color = []
result = []

for _ in range(N):
    color.append(list(sys.stdin.readline().rstrip()))


def findcolor(color):
    count1 = 0
    count2 = 0
    arr = []
    # case 1.
    for i in range(8):
        for j in range(8):
            if i % 2 == 0:
                if j % 2 == 0:
                    if color[i][j] != 'W':
                        count1 += 1
                elif j % 2 == 1:
                    if color[i][j] != 'B':
                        count1 += 1
            elif i % 2 == 1:
                if j % 2 == 0:
                    if color[i][j] != 'B':
                        count1 += 1
                elif j % 2 == 1:
                    if color[i][j] != 'W':
                        count1 += 1
    # case 2. 
    for k in range(8):
        for l in range(8):
            if k % 2 == 0:
                if l % 2 == 0:
                    if color[k][l] != 'B':
                        count2 += 1
                elif l % 2 == 1:
                    if color[k][l] != 'W':
                        count2 += 1
            elif k % 2 == 1:
                if l % 2 == 0:
                    if color[k][l] != 'W':
                        count2 += 1
                elif l % 2 == 1:
                    if color[k][l] != 'B':
                        count2 += 1
    arr.append(count1)
    arr.append(count2)
    return min(arr)


for i in range(N - 7):
    for j in range(M - 7):
        new_color = color[i:i + 8]
        for k in range(len(new_color)):
            new_color[k] = new_color[k][j:j + 8]
        result.append(findcolor(new_color))

print(min(result))
