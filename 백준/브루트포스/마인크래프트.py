# 1. 좌표 가장 위 블록 제거 : 2초
# 2. 좌표 가장 위에 블록 놓기 : 1초

n, m, b = map(int, input().split())  # b인벤토리에 들어있는 블록
ground = [list(map(int, input().split())) for _ in range(n)]

INF = int(1e9)
tall = 0
ans = INF

for i in range(257):  # 땅의 높이는 최대 256이므로 0~257까지만 탐색
    max = 0
    min = 0
    for j in range(n):  # 가로
        for k in range(m):  # 세로
            if ground[j][k] < i:  # 블럭이 현재 높이 보다 작다면
                min += (i - ground[j][k])  # 현재 높이가 블록 높이보다 높을 때 (min 만큼 인벤토리에서 꺼내서 채워야함)
            else:
                max += (ground[j][k] - i)  # 블록 높이가 현재 높이보다 높을 때 (max 만큼 블록이 제거된 후 인벤토리에 들어감)

    inventory = max + b  # 인벤토리에 있는 총 블록수 = 현재 인벤토리에 있는 블록 + max

    if inventory < min:  # 전부 채울 수 없으므로 패스
        continue

    time = 2 * max + min  # 블록 제거는 2초, 블록 추가는 1초

    if time <= ans:  # 높이는 0~256까지 오름차순으로 탐색하기 때문에 걸린 시간이 같아도 더 높은 높이가 출력된다.
        ans = time
        tall = i

print(ans, tall)
