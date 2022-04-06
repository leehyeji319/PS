from collections import deque

def solution(n, edges, k, a, b):
    answer = -1
    start = a
    end = b
    graph = [[] for i in range(n + 1)]
    queue = deque()
    
    for i in edges:
        x = i[0]
        y = i[1]
        graph[x].append(y)
        graph[y].append(x)
        
    visited = [False] * n

    def bfs(start, destination, visited):
        distance = [0] * n
        queue.append(start)
        visited[start] = True
        while queue:
            start = queue.popleft()
            for w in graph[start]:
                if destination in graph[start]:
                    w = destination
                if not visited[w]:
                    visited[w] = True
                    queue.append(w)
                    distance[w] = distance[start] + 1
                    if w == destination:
                        queue.clear()
                        return distance[w]
                    
    print(bfs(start, end, visited))

print(solution(8, [[0,1],[1,2],[2,3],[4,0],[5,1],[6,1],[7,2],[7,3],[4,5],[5,6],[6,7]], 4, 0, 3))