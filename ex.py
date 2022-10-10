import heapq
import sys

def input():
    return sys.stdin.readline().rstrip()

'''
 입력받는 과정
'''
N = int(input())
M = int(input())

board = [[] for _ in range(N + 1)]

for _ in range(M):
    fr, to, cost = map(int, input().split())
    board[fr].append((to, cost))

FROM, TO = map(int, input().split())

'''
 변수 설정
'''
distance = [float('inf') for _ in range(N+1)] # 거리
path = [[] for _ in range(N+1)] # 경로를 담을 배열
path[FROM].append(FROM)
q = [(0,FROM)] # 다익스트라를 쓸 우선순위 큐
heapq.heapify(q)


'''
 다익스트라를 이용한 알고리즘
'''
while q:
    now_cost, now = heapq.heappop(q)
    if now_cost > distance[now]:
        continue
    if now == FROM:
        distance[now] = 0
    for next, next_cost in board[now]:
        path_cost = next_cost + now_cost
        if path_cost < distance[next]:
            distance[next] = path_cost
            heapq.heappush(q, (path_cost, next))
            # path 가 갱신됐을 때 현재까지의 경로를 넣어준다.
            path[next] = []
            for p in path[now]:
                path[next].append(p)
            path[next].append(next)

print(path)

print(distance[TO])
print(len(path[TO]))
print(' '.join(map(str,path[TO]))) # 경로 출력