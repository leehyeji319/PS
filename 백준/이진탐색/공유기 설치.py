n, c = map(int, input().split())
arr = []
for _ in range(n):
    a = int(input())
    arr.append(a)
arr.sort()

start = 1
end = arr[-1] - arr[0] # 마지막이랑 처음의 거리 차이
result = 0 

while start <= end:
    mid = (start + end) // 2
    min = arr[0] # 제일 작은 배열 
    count = 1 # 공유기 설치된 개수 
    
    for i in range(1, len(arr)):
        if arr[i] >= min + mid: # 제일 작은 곳 + 중간값 더한 값보다 크다면 공유기 설치 가능
            count += 1 # 공유기를 설치했으니 +1 해주기
            min = arr[i] # 제일 작은 배열을 바꿔준다
    if count >= c:
        start = mid + 1
        result = mid
    else:
        end = mid - 1
        
print(result)

    