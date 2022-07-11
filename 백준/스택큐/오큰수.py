n = int(input())

arr = list(map(int, input().split()))
result = []
idx = 1
for a in range(len(arr)):
    m = max(arr[a: ])
    if a + idx == len(arr):
        result.append(-1)
        break
    if arr[a + idx] > arr[a]:
        result.append(arr[a + idx])
    elif arr[a + idx] < arr[a] and arr[a + idx] < m:
        if m == arr[a]:
            result.append(-1)
        else: result.append(m)
    else:
        result.append(-1)
        
print(result)