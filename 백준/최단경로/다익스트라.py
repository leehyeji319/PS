import sys
input = sys.stdin.readline
INF = int(1e9) #무한

#노드수, 간선수
n, m = map(int, input().split())
#시작노드
start = int(input())
#각 노드에 연결되어있는 노드에 대한 정보를 담는 리스트
board = [[] for i in range(n + 1)]
#방문한적이 있는지 확인하는 리스트
visited = [False] * (n + 1)
#최단거리 리스트를 모두 무한으로 초기화
distance = [INF] * (n + 1)

#모든 간선에 대한 정보를 입력받기 
for _ in range(m):
    a, b, c = map(int, input().split())
    #a노드에서 b노드로 가는 비용이 c
    board[a].append((b, c))

#방문하지 않은 노드중에서, 가장 최단 거리가 짧은 노드의 번호를 반환
def get_smallest_node():
    min_value = INF #제일 작은 값을 무한이라고 초기화
    index = 0 #가장 최단 거리가 짧은 노드(인덱스)
    for i in range(1, n + 1):
        if distance[i] < min_value and not visited[i]:
            min_value = distance[i]
            index = i
    return index

def dijkstra(start):
    #시작노드에대해서 초기화
    distance[start] = 0
    visited[start] = True
    for j in board[start]:
        distance[j[0]] = j[1]
    #시작 노드를 제외한 전체 n - 1개의 노드에 대해 반복
    for i in range(n - 1):
        #현재 최단 거리가 가장 짧은 노드를 꺼내서, 방문처리
        now = get_smallest_node()
        visited[now] = True
        #현재 노드와 연결된 다른 노드를 확인
        for j in board[now]:
            cost = distance[now] + j[1]
            #현재 노드를 거쳐서 다른 노드로 이동하는 거리가 더 짧은 경우
            if cost < distance[j[0]]:
                distance[j[0]] = cost

#다익스트라 알고리즘 수행
dijkstra(start)

#모든 노드로 가기위한 최단 거리를 출력
for i in range(1, n + 1):
    #도달할수없는 경우, INF라고 출력
    if distance[i] == INF:
        print("INF")
    #도달할수잇는 경우 출력
    else: print(distance[i])
