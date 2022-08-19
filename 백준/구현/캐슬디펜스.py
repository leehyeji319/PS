import sys
import itertools
import heapq

N, M, D = map(int, sys.stdin.readline().rstrip().split())
ARR = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(N)]
arr = []

castle_pos = [i for i in range(M)]
archer_cases = tuple(itertools.combinations(castle_pos, 3))
answer = 0

def get_enemy_cnt():
    global arr
    cnt = 0

    for i in range(N):
        for j in range(M):
            if arr[i][j] == 1: cnt+=1
    return cnt

def attack_enemy(archer_case_index):
    global arr
    remove_list = []
    attacked = [[False for _ in range(M)] for _ in range(N)]
    cnt = 0

    for archer_pos in archer_cases[archer_case_index]:
        pq = []

        for i in range(N - 1, -1, -1):
            for j in range(M):
                if arr[i][j] == 1:
                    distance = abs(N - i) + abs(archer_pos - j)
                    if distance <= D:
                        heapq.heappush(pq, [distance, j, i])
        if pq:
            _, x, y = heapq.heappop(pq)
            remove_list.append([y, x])

    for y, x in remove_list:
        if not attacked[y][x]:
            attacked[y][x] = True
            cnt+=1
            arr[y][x] = 0

    return cnt


def move_enemy():
    global arr
    arr[-1] = [0 for _ in range(M)]

    for i in range(-1, -N, -1):
        arr[i] = arr[i - 1]
    arr[0] = [0 for _ in range(M)]

def play(archer_case_index):
    cnt = 0
    
    while get_enemy_cnt() != 0:
        cnt += attack_enemy(archer_case_index)
        move_enemy()
    return cnt

for i in range(len(archer_cases)):
    arr = [[ARR[i][j] for j in range(M)] for i in range(N)]
    cnt = play(i)

    if answer < cnt : answer = cnt

print(answer)
