T = int(input())
for t in range(1, T + 1):
    answer = round(sum(list(map(int, input().split()))) / 10)
    print(f"#{t} {answer}")