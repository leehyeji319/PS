# https://www.acmicpc.net/problem/1406
import sys
string = list(sys.stdin.readline().rstrip())
M = int(sys.stdin.readline()) 
cursor = len(string)
result = list()

for i in range(M):
    order = sys.stdin.readline().rstrip()
    if order == 'L':
        if cursor > 0:
            cursor -= 1
    elif order == 'D':
        if cursor < len(string):
            cursor += 1
    elif order == 'B':
        if cursor > 0:
            cursor -= 1
            del string[cursor]
    else:
        string.insert(cursor, order[2])
        cursor += 1
for i in string:
    print(i, end='')