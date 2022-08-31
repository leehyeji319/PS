import sys
input = sys.stdin.readline
N, M, K = int(input().split())

fireball = []
for _ in range(M):
    r, c, m, s, d = map(int, input().split())
    fireball.append([r, c, m, s, d])
