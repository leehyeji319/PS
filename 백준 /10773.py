import sys

n = int(input())

stack = []

for i in range(n):
    num = int(sys.stdin.readline())
    if num != 0:
        stack.append(num)
    else: stack.pop()

print(sum(stack))
