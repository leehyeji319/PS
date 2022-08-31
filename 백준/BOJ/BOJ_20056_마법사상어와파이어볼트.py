import sys

input = sys.stdin.readline

N, M, K = int(input().split())  # N:격자크기 M:파이어볼개수 K:이동명령 횟수
direction = {0: (-1, 0), 1: (-1, 1), 2: (0, 1), 3: (1, 1), 4: (1, 0), 5: (1, -1), 6: (0, -1), 7: -(1, -1)}
graph = [[0] * N for _ in range(N)]
fireball = []
for _ in range(M):
    r, c, m, s, d = map(int, input().split())  # 행 열 질량 속력 방향
    graph[r, c] = M + 1
    fireball.append([r, c, m, s, d])

if M != len(fireball):
    fireball.append(fireball[0])

for i in range(K):
    for j in range(M):
        dir = graph[j][4]

        r = graph[j][0]
        c = graph[j][1]
        r += direction[dir][0]
        c += direction[dir][1]
