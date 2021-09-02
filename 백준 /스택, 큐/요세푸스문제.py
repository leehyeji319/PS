# https://www.acmicpc.net/problem/1158
from collections import deque

n, k = map(int, input().split())
queue = deque()
for i in range(1, n + 1):
    queue.append(i)

result = []

for i in range(n):
    for j in range(k - 1):
        queue.append(queue.popleft())
    result += [queue.popleft()]

print('<' + ', '.join(map(str, result)) + '>')