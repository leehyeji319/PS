
from collections import deque
#n노드수, m도로 개수, k최단거리조건, x출발노드
n, m, k, x = map(int, input().split())
#간선의 비용은 1
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
#모든 도시에 대해 최단거리 초기화
distance = [-1] * (n + 1)
#출발노드에선 거리가 0
distance[x] = 0

q = deque([x]) #출발노드부터 시작 ㅋㅋ 
while q:
    now = q.popleft()
    #현재 도시에서 이동할 수 있는 모든 도시를 확인
    for next_node in graph[now]:
        #아직 방문하지 않은 도시라면
        if distance[next_node] == -1:
            #최단거리 갱신
            distance[next_node] = distance[now] + 1
            q.append(next_node)

#최단 거리가 K인 모든 도시의 번호를 오름차순으로 출력
flag = False
for i in range(1, n + 1):
    if distance[i] == k:
        print(i)
        flag = True
if flag == False:
    print(-1) 



    