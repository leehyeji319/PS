import sys
import math

t = int(input())
room_arr = []
for _ in range(t):
    h, w, n = map(int, sys.stdin.readline().split())
    floor = n % h
    room = n // h + 1
    if n % h == 0:
        room = n // h
        floor = h
    print(f'{floor*100+room}')