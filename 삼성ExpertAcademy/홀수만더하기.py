T = int(input())
for t in range(1, T + 1):
    n = map(int, input().split())
    answer = sum([i for i in n if i % 2 == 1])
    print(f"#{t} {answer}")