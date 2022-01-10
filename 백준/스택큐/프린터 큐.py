#https://www.acmicpc.net/problem/1966
from collections import deque
t = int(input())
for i in range(t):
    n, m = map(int, input().split())
    # que = deque(list(map(int, input().split())))
    que = list(map(int, input().split()))
    cnt = 0
    idx = 0
    while que[m] != 0:
        if max(que) == que[idx%n]:
            que[idx%n] = 0
            cnt += 1
            idx += 1
        else:
            idx += 1
    print(cnt)