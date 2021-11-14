import sys
n = int(input())
arr = list(map(int, sys.stdin.readline().split()))
arr.sort()

left = 0
right = len(arr) - 1
answer = abs(arr[left] + arr[right])
left_ = left
right_ = right

while left < right:
    tmp = arr[left] + arr[right]
    if abs(tmp) < abs(answer):
        answer = tmp
        left_ = left
        right_ = right
        answer = abs(tmp)
        if answer == 0:
            break
    if tmp < 0: # tmp 값이 음수면 left + 1
        left += 1
    else:
        right -= 1 # tmp 값이 양수면 right - 1
        
print(arr[left_], arr[right_])


