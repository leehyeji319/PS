# https://www.acmicpc.net/problem/11866
from collections import deque
n, k = map(int, input().split())
que = deque()
for i in range(1, n + 1):
    que.append(i)

result = []

for i in range(n):
    for j in range(k - 1):
        que.append(que.popleft())
    result += [que.popleft()]

print('<' + ', '.join(map(str, result)) + '>')
