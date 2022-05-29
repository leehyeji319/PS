T = 10
for t in range(1, T + 1):
    n, arr_s = input().split()
    arr = [int(n) for n in str(arr_s)]
    stack = []
    idx = 0
    for i in range(len(arr)):
        if len(stack) == 0:
            stack.append(arr[i])
        elif len(stack) != 0 and stack[-1] == arr[i]:
            stack.pop()
        elif len(stack) != 0 and stack[-1] != arr[i]:
            stack.append(arr[i])
    print(f"#{t}", end=' ')
    for s in stack:
        print(s, end='')
    print()
