import sys
input = sys.stdin.readline

N, M = map(int, input().split()) #노드개수, 리프개수
tree = [[] for _ in range(N + 1)]
for i in range(M - 1):
    tree[i].append(M - 1)
for i in range(N - 1):
    i = M - 1
