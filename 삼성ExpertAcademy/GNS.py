s = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
dict = {}
for i, s in enumerate(s):
    dict[s] = i

T = int(input())
for t in range(1, T + 1):
    z = input()
    arr = list(input().split())
    arr.sort(key = lambda x: dict[x])
    print(f"#{t}")
    for a in arr:
        print(a, end=' ')