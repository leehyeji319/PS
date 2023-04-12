from itertools import combinations
while True:
    li = list(map(int, input().split()))
    if len(li) == 1 and li[0] == 0:
        exit()
    k = li[0]
    s = li[1:]

    for comb in combinations(s, 6):
        ans = list(comb)
        for a in ans:
            print(a, end=" ")
        print()

    print()



