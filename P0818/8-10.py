# 다이나믹 프로그래밍 : 병사 배치하기. 열외 시켜야 하는 병사의 수를 출력하는 프로그램을 작성하시오
# 이 문제의 기본 아이디어는 가장 긴 증가하는 부분 수열(Longet Increasing Subsequence)로 알려진 전형적인 dp문제 
# 가장 긴 증가하는 부분수열 알고리즘을 확인합시다.
# D[i] = array[i]를 마지막 원소로 가지는 부분 수열의 최대 길이
# 점화식 : 모든 O <= j < i 에 대하여, D[i] = max(D[i], d[j] + 1) if array[j] < array[i]

n = int(input())
array = list(map(int, input().split()))
# 순서를 뒤집어 '최장 증가 부분 수열' 문제로 변환
array.reverse()

# 다이나믹 프로그래밍을 위한 1차원 DP 테이블 초기화
dp = [1] * n

# 가장 긴 증가하는 부분 수열(lis) 알고리즘 수행
for i in range(1, n):
    for j in range(0, i):
        if array[j] < array[i]:
            dp[i] = max(dp[i], dp[j] + 1)

# 열외해야 하는 병사의 최소 수를 출력
print(n - max(dp))