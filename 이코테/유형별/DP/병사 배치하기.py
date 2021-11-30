# 가장 긴 증가하는 부분 수열 - 전형적인 다이나믹 프로그래밍 문제 (LIS)
# 가장 긴 감소하는 부분 수열을 찾는 문제
# lis 알고리즘을 뒤집어서 수행하면 답이 된다
n = int(input())
array = list(map(int, input().split()))
# 순서를 뒤집어 '최장 증가 부분 수열' 문제로 변환
array.reverse()

# 다이나믹 프로그래밍을 위한 1차원 dp테이블 초기화
dp = [1] * n

# 가장 긴 증가하는 부분 수열(lis) 알고리즘 수행
for i in range(1, n):
    for j in range(0, i):
        if array[j] < array[i]:
            dp[i] = max(dp[i], dp[j] + 1)

# 열외해야하는 병사의 최소 수를 출력한다
print(n - max(dp))
