T = int(input())
for t in range(1, T + 1):
    N = int(input())
    mid = N // 2
    farm = [list(map(str, input())) for _ in range(N)]
    farm = [list(map(int, n)) for n in farm]
    sum_all = 0
    for i in range(N // 2 + 1):
        sum_up = sum(farm[mid - i][i: N - i])
        sum_down = sum(farm[mid + i][i: N - i])
        sum_all += (sum_up + sum_down)
    answer = sum_all - sum(farm[mid])
    print(f"#{t} {answer}")