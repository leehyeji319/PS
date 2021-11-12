import sys

n = int(input())
arr = list(map(int, sys.stdin.readline().split()))
arr.sort()
left = 0 
right = len(arr) - 1
target = int(input())
cnt = 0
while left < right:
    if arr[left] + arr[right] == target:
        cnt += 1
    elif arr[left] + arr[right] < target:
        left += 1
        continue
    right -= 1
    
print(cnt)
    
        
