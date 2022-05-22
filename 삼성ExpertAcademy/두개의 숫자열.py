T = int(input())
for t in range(1, T + 1):
    N, M = map(int, input().split())
    arr_a = list(map(int, input().split()))
    arr_b = list(map(int, input().split()))
    sum = 0
    max_a = max(arr_a)
    min_a = min(arr_a)
    max_b = max(arr_b)
    min_b = min(arr_b)

    if len(arr_a) == len(arr_b):
        for a, b in zip(arr_a, arr_b):
            sum += (a * b)
    if len(arr_a) > len(arr_b):
        pass
