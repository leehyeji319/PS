import sys

n = int(input())
l = []
for _ in range(n):
    l.append(list(map(int, sys.stdin.readline().split())))

l.sort()

for i in l:
    for j in i:
        print(j, end=' ')
    print()