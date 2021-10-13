import sys
n = int(input())
list = []
for _ in range(n):
    list.append(int(sys.stdin.readline()))
for i in sorted(list):
    sys.stdout.write(str(i)+'\n')
