T = int(input())
for t in range(1, T + 1):
    original = [int(n) for n in list(input())]
    stack = []
    cnt = 0
    for o in original:
        if len(stack) != 0:
            if o != stack[-1]:
                cnt += 1
                stack.append(o)
        else:
            stack.append(o)
            cnt += 1
    if stack[0] == 0:
        cnt -= 1
    print(f"#{t} {cnt}")