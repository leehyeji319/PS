#1=N 2=S 위에가 N극 아래가 S극
T = 10
for t in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    cnt = 0
    stack = []
    for i in range(N):
        magnet = []
        for j in range(N):
            if arr[j][i] == 1 or arr[j][i] == 2:
                magnet.append(arr[j][i])
        stack = []
        for m in magnet:
            if m == 1:
                stack.append(1)
            elif m == 2:
                if len(stack) == 0:
                    continue
                else:
                    stack.pop()
                    cnt += 1

    print(f"#{t} {cnt}")