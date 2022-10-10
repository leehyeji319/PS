import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

# 노드 개수 간선 개수 입력받기
V, E = map(int, input().split())
start = int(input())
# 각 노드에 연결된 정보를 담는 리스트 생성
board = [[] for _ in range(V + 1)]
# 최단 거리 테이블 초기화
distance = [INF] * (V + 1)

# 간성 정보 입력 받기
for _ in range(E):
    u, v, w = map(int, input().split())
    board[u].append((v, w))

def dijkstra(start):
    q = [] #우선순위 큐
    # 시작 노드로 가기 위한 최단 경로는 0으로 설정해서 큐에 삽입
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        #가장 최단 거리가 짧은 노드에 대한 정보 꺼내기
        dist, now = heapq.heappop(q)
        #현재 노드가 처리 된 적 있는 노드라면 무시
        if distance[now] < dist:
            continue
        #현재 노드와 연결된 다른 인접한 노드들을 확인
        for i in board[now]:
            cost = dist + i[1] #거리값
            #현재 노드를 거쳐서, 다른 노드로 이동하는 거리가 더 짧은 경우
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

dijkstra(start)

#모든 노드로 가기 위한 최단 거리를 출력
for i in range(1, V + 1):
    #도달할 수 없는 경우 무한이라고 출력
    if distance[i] == INF:
        print("INF")
    else:
        print(distance[i])