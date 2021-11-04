# N가지 종류의 화폐가 있을때, 이 화폐들의 개수를 최소한으로 이용해서 그 가치의 합이 M원이 되도록 하여라 
# M원을 만들기 위한 최소한의 화폐 개수를 출력
# ai 금액 i를 만들 수 있는 최소한의 화폐 개수
# 각 화페의 단위 
# 점화식 : 각 화폐 단위인 k를 하나씩 확인하며   ai = min(ai, ai-k + 1)
# 일단 무한으로 리스트 초기화
N, M = map(int, input().split())
money = []
for _ in range(N):
    money.append(input())

# 한 번 계산된 결과를 저장하기 위한 DP 테이블 초기화
d = [10001] * (M + 1)
#dp bottom up
d[0] = 0
for i in range(N): # 모든 금액을 확인하며
    for j in range(money[i], M + 1):
        # 현재 금액에서 현재 확인하고 있는 화폐 단위 금액을 뺀, 그 금액을 만들 수 있따면
        if d[j - money[i]] != 10001: # (i - k)원을 만드는 방법이 존재하는 경우
            d[j] = min(d[j - money[i]] + 1)
# 계산된 결과 출력
if d[M] == 10001: # 최종적으로 M원을 만드는 방법이 없는 경우
    print(-1)
else:
    print(d[M])