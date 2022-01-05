import sys
n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())
arr_ = list(map(int, sys.stdin.readline().split()))
result = []
arr.sort()

for i in arr_:
    Flag = False
    start, end = 0, len(arr) - 1
    
    while start <= end:
        mid = (start + end) // 2
        if i > arr[mid]:
            start = mid + 1
        elif i < arr[mid]:
            end = mid - 1
        elif i == arr[mid]:
            print("1", end=" ")
            Flag = True
            break;
    if Flag == False:
        print("0", end=" ")
# 숫자의 범위가 크기 때문에 이진탐색으로 풀 수 있다.
