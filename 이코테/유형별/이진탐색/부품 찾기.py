def binary_search(arr, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if arr[mid] == target:
            return 1
        elif arr[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return 0

n = int(input())
l = sorted(list(map(int, input().split())))
m = int(input())
find_l = list(map(int, input().split()))
answer = []
for f in find_l:
    result = binary_search(l, f, 0, n - 1)
    if result == 1:
        answer.append('yes')
    else: answer.append('no')
for i in answer:
    print(i, end=' ')