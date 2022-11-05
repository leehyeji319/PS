from collections import deque

def solution(worldmap):
    answer = 0

    N = len(worldmap)
    M = len(worldmap[0])

    map = list([0] * M for _ in range(N))

    for i in range(N):
        for j in range(M):
            map[i][j] = worldmap[i][j]

    # 상하좌우 대각선 왼위아 오위아
    status = 3

    dr = [-1, 1, 0, 0, -1, 1, -1, 1]
    dc = [0, 0, -1, 1, -1, -1, 1, 1]

    def bfs(r, c):
        queue = deque()
        queue.append((r, c))

        while queue:
            r, c = queue.popleft()
            for d in range(8):
                nr = r + dr[d]
                nc = c + dc[d]

                if nr >= N or nc >= M or nr < 0 or nc < 0:
                    continue
                if map[nr][nc] == "X":
                    continue



    print(map)

    return answer

print(solution(["..XXX", "..XXX", "...XX", "X....", "XXX.."]))