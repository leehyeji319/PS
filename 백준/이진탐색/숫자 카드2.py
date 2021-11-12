import sys
from collections import Counter

def binary_search(arr, target, start, end):
    if start > end: 
        return 0
    mid = (start + end) // 2
    if arr[mid] == target:
        return 1
    elif arr[mid] > target:
        return binary_search(arr, target, start, mid - 1)
    else:
        return binary_search(arr, target, mid + 1, end)
    
n = int(input())
arr = list(map(int, sys.stdin.readline().split()))
cnt = Counter(arr) # 원소의 개수
arr = list(set(arr)) # 정렬 
arr.sort()



m = int(input())
find_arr = list(map(int, sys.stdin.readline().split()))
r = []

for a in find_arr:
    result = binary_search(arr, a, 0, len(arr) - 1) # set하고 난 이후니까 길이가 다름..
    if result == 0:
        r.append(0)
    else:
        r.append(cnt[a])

for i in r:
    print(i, end=' ')