# https://www.acmicpc.net/problem/2164
import sys
from collections import deque
que = deque([])

n = int(input())
for i in range(1, n + 1):
    que.append(i)

while True:
    if len(que) == 1:
        break
    else: 
        que.popleft()
        que.append(que.popleft())
print(que[0])