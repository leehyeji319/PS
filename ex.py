import sys
from itertools import permutations

input = sys.stdin.readline

N = int(input())
max_total = -1
innings = [list(map(int, input().split())) for _ in range(N)]

for perm in permutations(range(1, 9), 8):
    perm = list(perm[:3]) + [1] + list(perm[3:])
    total = 0
    idx = 0

    for inning in innings:
        out = 0
        base1, base2, base3 = 0, 0, 0
        while out < 3:
            if inning[perm[idx]] == 1:
                total += base3
                base1, base2, base3 = 1, base1, base2
            elif inning[perm[idx]] == 2:
                total += (base2 + base3)
                base1, base2, base3 = 0, 1, base1
            elif inning[perm[idx]] == 3:
                total += (base1 + base2 + base3)
                base1, base2, base3 = 0, 0, 1
            elif inning[perm[idx]] == 4:
                total += (1 + base1 + base2 + base3)
                base1, base2, base3 = 0, 0, 0
            elif inning[perm[idx]] == 0:
                out += 1

            idx = (idx + 1) % 9

    max_total = max(max_total, total)
print(max_total)