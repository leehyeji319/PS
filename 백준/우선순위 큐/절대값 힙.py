import sys
import heapq

n = int(input())
h = []

for i in range(n):
    a = int(sys.stdin.readline())
    if a != 0:
        heapq.heappush(h, (abs(a), a))
        # heap을 튜플로 구성했을때 맨 앞 숫자만 가지고 정렬하므로 앞은 abs 두번째 원래수
    else:
        if len(h) == 0:
            print(0)
        else:
            print(heapq.heappop(h)[1])
    