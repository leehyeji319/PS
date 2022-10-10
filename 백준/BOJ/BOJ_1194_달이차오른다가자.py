import sys
input = sys.stdin.readline

N, M = map(int, input().split())

board = [list(input().rstrip()) for _ in range(N)]

keys = ['a', 'b', 'c', 'd', 'e', 'f']
doors = ['A', 'B', 'C', 'D', 'E', 'F']
