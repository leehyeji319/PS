T = int(input())

for t in range(1, T + 1):
    a, b = map(int, input().split())
    answer = divmod(a, b)
    share = answer[0]
    remainder = answer[1]
    print(f"#{t} {share} {remainder}")