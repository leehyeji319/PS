T = 10
for t in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))
    idx = 0
    cycle = 1
    while True:
        idx %= 8
        cycle %= 5
        if cycle == 0:
            cycle = 5
        arr[idx] -= cycle
        if arr[idx] <= 0:
            arr[idx] = 0
            idx += 1
            break
        idx += 1
        cycle += 1

    answer = arr[idx:] + arr[:idx]

    print(f"#{t}", end=' ')
    for a in answer:
        print(a, end=' ')
    print()