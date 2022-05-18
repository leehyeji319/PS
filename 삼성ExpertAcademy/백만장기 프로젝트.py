T = int(input())
for t in range(T):
    n = int(input())
    arr = list(map(int, input().split()))
    m = arr[-1]
    answer = 0
    for i in range(len(arr) - 1, -1, -1):
        if arr[i] <= m:
            answer += (m - arr[i])
        elif arr[i] > m:
            m = arr[i]
    #print("#{} {}".format(t + 1, answer))
    print(f"#{t + 1} {answer}")