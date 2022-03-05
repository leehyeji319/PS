n = int(input())
c = []

for _ in range(n):
    c.append(list(map(int, input().split())))

for i in range(1, len(c)):
    # c[i][0] 은 i번째 집을 빨강으로 칠했을때의 최솟값
    c[i][0] = min(c[i - 1][1], c[i - 1][2]) + c[i][0]
    c[i][1] = min(c[i - 1][0], c[i - 1][2]) + c[i][1]
    c[i][2] = min(c[i - 1][0], c[i - 1][1]) + c[i][2]

print(min(c[n - 1][0], c[n - 1][1], c[n - 1][2]))