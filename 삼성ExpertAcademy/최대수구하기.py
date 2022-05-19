T = int(input())
for t in range(1, T + 1):
    answer = max(map(int, input().split()))
    print(f"#{t} {answer}")