# 임의의 두 정점을 반드시 통과해야한다. 
# 한번 이동했던 정점, 한번 이동했던 간선도 다시 이동가능 but 최단거리를 이용해야함
import sys
import heapq

input = sys.stdin.readline
INF = int(1e9)

n, e = map(int, input().split())

graph = [[] for _ in range(n + 1)]

#노드 간선 정보
for _ in range(e):
    a, b, c = map(int, input().split())
    #무방향 그래프
    graph[a].append((b, c))
    graph[b].append((a, c))
    
#반드시 거쳐야하는 노드 정보
v1, v2 = map(int, input().split())

def dijkstra(start):
    distance = [INF] * (n + 1)
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    
    while q: #큐가 비어있지 않다면
        #가장 최단 거리가 짧은 노드에 대한 정보 꺼내기
        dist, now = heapq.heappop(q)
        #현재 노드와 연결된 다른 인접한 노드를 확인
        if distance[now] < dist:
            continue
        #현재 노드와 연결된 다른 인접한 노드를 확인
        for i in graph[now]:
            cost = dist + i[1]
            #현재 노드를 거쳐서, 다른 노드로 이동하는 거리가 더 짧은 경우
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))
    return distance

original_distance = dijkstra(1)
v1_distance = dijkstra(v1)
v2_distance = dijkstra(v2)

way1 = original_distance[v1] + v1_distance[v2] + v2_distance[n]
way2 = original_distance[v2] + v2_distance[v1] + v1_distance[n]

if way1 == INF and way2 == INF:
    print(-1)
else: 
    print(min(way1, way2))