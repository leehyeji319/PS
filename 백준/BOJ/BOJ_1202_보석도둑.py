ㅐㅓimport sys
import heapq

input = sys.stdin.readline
N, K = map(int, input().split())  # 보석개수, 가방개수

# 보석무게, 가격
jewels = []
for _ in range(N):
    heapq.heappush(jewels, list(map(int, input().split())))
# 각 가방 가능 무게
bags = [int(input()) for i in range(K)]

bags.sort()
# print(jewels)
answer = 0
able = []
# 가능한 가방은 힙으로 사용
for i in range(len(bags)):
    # 현재보고있는 가방
    now_bag = bags[i]
    # 현재가방에 넣을 수 있는 후보 넣기
    while jewels and now_bag >= jewels[0][0]:
        heapq.heappush(able, -heapq.heappop(jewels)[1])
    if able:
        answer -= heapq.heappop(able)
    elif not jewels:
        break
print(answer)
