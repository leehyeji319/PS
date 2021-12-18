import heapq
import sys

n = int(input())
h = []
for i in range(n):
    a = int(sys.stdin.readline())
    if a != 0:
        heapq.heappush(h, (-a))
    else:
        if len(h) == 0:
            print(0)
        else:
            print(-1 * heapq.heappop(h))