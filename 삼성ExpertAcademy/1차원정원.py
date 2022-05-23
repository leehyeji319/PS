T = int(input())
for t in range(1, T + 1):
    N, D = map(int, input().split())
    D = D * 2 + 1
    answer = 0
    arr = divmod(N, D)
    if arr[1] != 0:
        answer += arr[0] + 1
    else:
        answer = arr[0]
    print(f"#{t} {answer}")
