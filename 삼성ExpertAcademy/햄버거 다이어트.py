from itertools import combinations

T = int(input())
for t in range(1, T + 1):
    n, limit_calories = map(int, input().split())
    materials = [list(map(int, input().split())) for _ in range(n)]

    max_score = 0
    for i in range(1, n + 1):
        for value in combinations(materials, i):
            kcal = 0
            score = 0
            for v in range(len(value)):
                kcal += value[v][1]
                score += value[v][0]
            if kcal > limit_calories:
                continue
            if max_score < score:
                max_score = score

    print(f"#{t} {max_score}")