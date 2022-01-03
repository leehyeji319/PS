# 시간초과
# binary search 방법이 아니잔아 다시풀기
# LIS 는 이코테 - DP - 병사 배치 문제 참고

N = int(input())
arr = list(map(int, input().split()))

dp = [1 for i in range(N)]

for i in range(N):
    for j in range(i):
        if arr[i] > arr[j]:
            dp[i] = max(dp[i], dp[j] + 1)
            
print(max(dp))

# 뒤집지 않은 문제 