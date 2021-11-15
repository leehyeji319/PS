k, n = map(int, input().split())
arr = []
for _ in range(k):
    a = int(input())
    arr.append(a)
arr.sort()

start = 1
end = max(arr)

result = 0
while (start <= end):
    total = 0
    mid = (start + end) // 2
    for x in arr:
        total += x // mid
    if total < n: # 자른 갯수가 n보다 적으면
        end = mid - 1
    # 랜선의 양이 충분한 경우 덜 자르기(오른쪽 탐색)
    else:
        start = mid + 1
print(end)
