# 0은 검정 못가는 부분 1은 갈수있는 부분

T = int(input())
for t in range(1, T + 1):
    N, K = map(int, input().split())
    graph = [list(map(int, input().split())) for _ in range(N)]
    answer = 0

    for i in range(N):
        cnt = 0
        # 행을 검사
        for j in range(N):
            if graph[i][j] == 1:
                cnt += 1
            if graph[i][j] == 0 or j == N - 1:
                if cnt == K:
                    answer += 1
                cnt =0

        # 열을 검사
        for j in range(N):
            if graph[j][i] == 1:
                cnt += 1
            if graph[j][i] == 0 or j == N - 1:
                if cnt == K:
                    answer += 1
                cnt = 0
    print(f"#{t} {answer}")

