T = int(input())
for t in range(1, T + 1):
    L, U, X = map(int, input().split())
    if X < L:
        print(f"#{t} {L - X}")
    elif L <= X <= U:
        print(f"#{t} 0")
    else:
        print(f"#{t} -1")