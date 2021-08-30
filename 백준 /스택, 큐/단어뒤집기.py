# https://www.acmicpc.net/problem/9093


# n = int(input())
# for i in range(n):
#     string = input()
#     string += "\n"
#     stack = []
#     for j in string:
#         if j == " " or j == '\n':
#             while stack:
#                 print(stack.pop(), end='')
#             print(' ', end='')
#         else:
#             stack.append(j)
#     print()

import sys


s = int(input())
for i in range(s):
    string = list(sys.stdin.readline().split())
    for j in string:
        print(j[::-1], end=' ')
    print()
