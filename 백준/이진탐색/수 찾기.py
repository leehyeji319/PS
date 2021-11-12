def binary_search(array, target, start, end):
    if start > end:
        return 0
    mid = (start + end) // 2
    if array[mid] == target:
        return 1
    elif array[mid] > target:
        return binary_search(array, target, start, mid - 1)
    else: 
        return binary_search(array, target, mid + 1, end)

n = int(input())
array = list(map(int, input().split()))
array.sort()

m = int(input())
c_array = list(map(int, input().split()))

for a in c_array:
    result = binary_search(array, a, 0, n - 1)
    if result == 1:
        print(1)
    else:
        print(0)

    
