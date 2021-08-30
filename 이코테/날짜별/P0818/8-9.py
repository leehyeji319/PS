 # 다이나믹 프로그래밍 : 금광 문제
# array[i][j] = i행 j열에 존재하는 금의 양
# dp[i][j] = i행 j열까지의 최적의 해 (얻을 수 있는 금의 최댓값)
# 점화식 : dp[i][j] = array[i][j] + max(dp[i- 1][j - 1], dp[i][j - 1], dp[i + 1][j - 1])
# 이때 테이블에 접근할 때마다 리스트의 범위를 벗어나지 않는지 체크해야 합니다.
# 편의상 초기 데이터를 담는 변수 array를 사용하지 않아도 됩니다. 바로 dp테이블에 초기 데이터를 담아서 다이나믹 프로그래밍을 적용

#테스트 케이스(TEst Case) 입력
for tc in range(int(input())):
    # 금광 정보 입력
    n, m = map(int, input().split())
    array = list(map(int, input().split()))
    # 다이나믹 프로그래밍을 위한 2차원 DP테이블 초기화
    dp = []
    index = 0
    for i in range(n):
        dp.append(array[index:index + m])
        index += m
    # 다이나믹 프로그래밍 진행
    for j in range(1, m):
        for i in range(n):
            # 왼쪽 위에서 오는 경우
            if i == 0: left_up = 0
            else: left_up = dp[i + 1][j - 1]
            # 왼쪽 아래에서 오는 경우
            if i == n - 1: left_down = 0
            else: left_down = dp[i + 1][j - 1]
            # 왼쪽에서 오는 경우
            left = dp[i][j - 1]
            dp[i][j] = dp[i][j] + max(left_up, left_down, left)
        result = 0
        for i in range(n):
            result = max(result, dp[i][m - 1])
        print(result)
