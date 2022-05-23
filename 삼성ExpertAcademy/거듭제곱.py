T = 10
for t in range(1, T + 1):
    a = int(input())
    N, M = map(int, input().split())
    print(f"#{t} {N ** M}")