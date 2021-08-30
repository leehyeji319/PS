# https://www.acmicpc.net/problem/9012

N = int(input())

for i in range(N):
    string = input()
    stack = []
    count = 0 # 스택의 크기
    isVPS = True

    for j in string:
        if j == '(':
            stack.append(j)
            count += 1
        elif j == ')':
            if len(stack) == 0:
                print("NO")
                isVPS = False
                break
            else:
                stack.pop()
                count -= 1

    if isVPS == True:
        if len(stack) == 0 and count == 0:
            print("YES")
        elif len(stack) != 0 and count != 0:
            print("NO")
