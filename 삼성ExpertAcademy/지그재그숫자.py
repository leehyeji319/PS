T = int(input())
for t in range(1, T + 1):
    n = int(input())
    answer = 0
    for i in range(1, n + 1):
        if i % 2 == 0:
            answer -= i
        else:
            answer += i
    print(f"#{t} {answer}")
