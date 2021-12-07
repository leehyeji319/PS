n, m = map(int, input().split())
arr = list(map(int, input().split()))

start = 1
end = max(arr)

while(start <= end):
    total = 0
    mid = (start + end) // 2
    
    for x in arr:
        if x > mid:
            total += x - mid
        
    if total >= m:
        start = mid + 1
    else:
        end = mid - 1
        
print(end)