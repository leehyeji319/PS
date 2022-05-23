#d2
T = 10
for t in range(1, T+ 1):
    N = int(input())
    building = list(map(int, input().split()))
    i = 2
    count = 0
    while i <= N - 3:
        if building[i] >= building[i + 1] and building[i] >= building[i + 2] and building[i] >= building[i - 1] and building[i] >= building[i - 2]:
            near_tall_building = max(building[i + 1], building[i + 2], building[i - 1], building[i - 2])
            count += building[i] - near_tall_building
            i += 2
        else:
            i += 1
    print(f"#{t} {count}")