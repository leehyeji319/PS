import itertools

T = int(input())
for t in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))
    sum = 0
    for p in list(itertools.permutations(arr, 2)):
        sum += p[0] % p[1]
    print(f"#{t} {sum}")
