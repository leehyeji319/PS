from collections import deque

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


N = int(input())
graph = [list(map(int, input().strip())) for _ in range(N)]
answer = []

def bfs(sr, sc):
    q = deque()
    q.append((sr, sc))
    graph[sr][sc] = 0
    house_cnt = 1

    while q:
        r, c = q.popleft()
        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]

            if nr >= N or nc >= N or nr < 0 or nc < 0:
                continue

            if graph[nr][nc] == 1:
                graph[nr][nc] = 0
                q.append((nr, nc))
                house_cnt += 1
    return house_cnt

for i in range(N):
    for j in range(N):
        if graph[i][j] == 1:
            answer.append(bfs(i, j))

answer.sort()

print(len(answer))
for a in answer:
    print(a)
