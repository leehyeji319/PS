import sys
N = int(input())
add = 0 # 추가 대야하는 거
op = '' # 연산자 + - 
stack = []

for i in range(N):
    a = int(input())
    if a > add:
        while a > add:
           add += 1
           stack.append(add)
           op += '+'
        stack.pop()
        op += '-'
    else:
        if stack[-1] != a:
            print("NO")
            sys.exit(0)
        else:
            stack.pop()
            op += '-'

for i in op:
    print(i)

# ㅅㅡ태ㄱ 수ㄹ
