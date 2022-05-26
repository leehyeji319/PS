from collections import deque

N, M, V = map(int, input().split())

graph = [[] for _ in range(N + 1)]
for i in range(N):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
print(graph)

for i in range(len(graph)):
    graph[i].sort()


# bfs 예제 
def bfs(graph, start, visited):
    # 큐 구현을 위해 deque 라이브러리 사용
    queue = deque([start])
    # 현재 노드를 방문 처리
    visited[start] = True
    # 큐가 빌때까지 반복
    while queue:
        # 큐에서 하나의 원소를 뽑아 출력
        v = queue.popleft()
        print(v, end=' ')
        # 해당 원소와 연결된, 아직 방문하지 않은 원소들을 큐에 삽입
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

visited = [False] * (N + 1)
bfs(graph, V, visited)