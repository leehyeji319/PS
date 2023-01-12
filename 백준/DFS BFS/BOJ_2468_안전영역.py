from collections import deque

N = int(input())
graph = []
max_v = -1

for _ in range(N):
    l = list(map(int, input().split()))
    max_v = max(max(l), max_v)
    graph.append(l)

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def bfs(s_r, s_c, num):
    q = deque()
    q.append((s_r, s_c))
    visited[s_r][s_c] = 1

    while q:
        r, c = q.popleft()

        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]

            if 0 <= nr < N and 0 <= nc < N and visited[nr][nc] == 0 and graph[nr][nc] > num:
                visited[nr][nc] = 1
                q.append((nr, nc))


result = 0
for i in range(max_v):
    visited = [[0] * N for _ in range(N)]
    count = 0
    for j in range(N):
        for k in range(N):
            if graph[j][k] > i and visited[j][k] == 0:
                bfs(j, k, i)
                count += 1

    if result < count:
        result = count
print(result)


