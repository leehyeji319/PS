from collections import Counter

T = int(input())
for t in range(1, T + 1):
    n = int(input())
    arr = input().split()
    answer = Counter(arr).most_common(1)
    print(f"#{t} {answer[0][0]}")
