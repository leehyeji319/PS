#https://www.acmicpc.net/problem/1021
from collections import deque

n, m = map(int, input().split())
deque = deque([i for i in range(1, n + 1)])
target = list(map(int, input().split()))
cnt = 0
for i in target:
    while True:
        if deque[0] == i:
            deque.popleft()
            break
        else:
            if deque.index(i) < len(deque) - deque.index(i):
                while deque[0] != i:
                    deque.append(deque.popleft())
                    cnt += 1
            else:
                while deque[0] != i:
                    deque.appendleft(deque.pop())
                    cnt += 1
print(cnt)
        