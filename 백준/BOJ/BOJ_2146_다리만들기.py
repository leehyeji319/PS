#https://www.acmicpc.net/problem/2146

import sys
from copy import deepcopy

input = sys.stdin.readline

def island_edge_dfs(r, c):
    if r <= -1 or r >= N or c <= -1 or c >= N:
        return False
    if visited_map[r][c] == 0:
        map[r][c] = 1
        #상하좌우
        island_edge_dfs(r - 1, c)
        island_edge_dfs(r, c - 1)
        island_edge_dfs(r + 1, c)
        island_edge_dfs(r, c + 1)
        return True
    return False

    pass

N = int(input())

map = [list(map(int, input().split())) for _ in range(N)]
visited_map = deepcopy(map)
islands_edges = []


dr = [1, -1, 0, 0]
dc = [0, 0, -1, 1]
