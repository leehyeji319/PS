T = int(input())

for tc in range(1, T + 1):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    if n > m:
        x, y = b, a
    else:
        x, y = a, b

    sums = []
    for i in range(abs(n - m) + 1):
        sum = 0
        for j in range(len(x)):
            sum += x[j] * y[i + j]
        sums.append(sum)
    print(f"#{tc}", max(sums))