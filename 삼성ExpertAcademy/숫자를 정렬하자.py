T = int(input())
for t in range(1, T + 1):
    n = int(input())
    arr = list(map(int, input().split()))
    arr.sort()
    print(f"#{t}", end=" ")
    for a in arr:
        print(a, end=" ")
    print()