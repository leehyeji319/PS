import sys

arr = []
remain = []

for i in range(10):
    a = int(sys.stdin.readline().rstrip())
    arr.append(a)

for j in arr:
    remain.append(j % 42)

print(len(set(remain)))
