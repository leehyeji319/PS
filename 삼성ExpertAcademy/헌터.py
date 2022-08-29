from itertools import permutations
import sys

input = sys.stdin.readline


def calc(perm, total, visited):
    global result

    for i in range(len(perm)):
        if perm[i][0] > 0:
            visited[perm[i][0] - 1] = True
        if perm[i][0] < 0 and not visited[abs(perm[i][0]) - 1]:
            return

    # 여기까지 왔으면 가치지기 된것
    # 헌터부터 유클리드거리 더해주고,
    total += (perm[0][1] + perm[0][2])
    for i in range(len(perm) - 1):
        total += (abs(perm[i][1] - perm[i + 1][1]) + abs(perm[i][2] - perm[i + 1][2]))

    if result > total:
        result = total


T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    graph = [list(map(int, input().split())) for _ in range(N)]
    monster_info = []
    person_info = []
    all_info = []
    for i in range(N):
        for j in range(N):
            if graph[i][j] > 0:
                monster_info.append([graph[i][j], i, j])
            elif graph[i][j] < 0:
                person_info.append([graph[i][j], i, j])

    result = int(1e9)
    all_info = monster_info + person_info

    for perm in list(permutations(all_info)):
        perm = list(perm)
        # print(perm)
        visited = [False] * len(monster_info)
        calc(perm, 0, visited)

    print(f"#{tc} {result}")
