#1=N 2=S 위에가 N극 아래가 S극
T = 10
for t in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    answer = 0
    for i in range(N):
        magnet = [arr[j][i] for j in range(N) if arr[j][i] == 1 or arr[j][i] == 2]
        stack = []
        for m in magnet:
            if len(stack) == 0:
                stack.append(m)
            else:
                if stack[-1] == m:
                    continue
                elif stack[-1] != m:
                    stack.append(m)
        if len(stack) == 1:
            continue
        if stack[0] == 2:
            stack = stack[1:]
        if stack[-1] == 1:
            stack = stack[:-1]
        answer += len(stack) // 2

    print(f"#{t} {answer}")