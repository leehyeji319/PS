# array[i][j] = i행 j열에 존재하는 금의 양
# dp[i][j] = i행 j열까지의 최적의 해 (얻을 수 있는 금의 최댓값)
# 점화식 : dp[i][j] = array[i][j] + max(dp[i - 1][j - 1], dp[i][j - 1], dp[i + 1][j - 1])
# 테이블에 접근할 때마다 리스트의 범위를 벗어나는지 확인
# array 사용안하고 그냥 바로 dp테이블에 초기화해서 사용한다

# test case input
for tc in range(int(input())):
    # 금광 정보 입력
    n, m = map(int, input().split())
    array = list(map(int, input().split()))
    # dp table 초기화
    dp = []
    index = 0
    for i in range(n):
        dp.append(array[index:index + m])
        index += m
    # 다이나믹 프로그래밍 진행
    for j in range(1, m):
        for i in range(n):
            # 왼쪽에서 오는 경우
            if i == 0: left_up = 0 #인덱스 벗어나는지 체크
            else: left_up = dp[i - 1][j - 1]
            # 왼쪽 아래에서 오는 경우
            if i == n - 1: left_down = 0 # 인덱스 벗어나는지 체크
            else: left_down = dp[i + 1][j - 1]
            # 왼쪽에서 오는 경우
            left = dp[i][j - 1]
            dp[i][j] = dp[i][j] + max(left_up, left_down, left)
    result = 0
    for i in range(n):
        result = max(result, dp[i][m - 1]) # 제일 큰 값을 찾기
    print(result)