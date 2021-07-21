# 시각 : 시각에서 3이 포함된 시간 다 구하기
#전형적인 완전탐색 문제(Brute Forcing)
#가능한 경우의 수를 모두 검사해보는 탐색 방법

# h입력 받기
h = int(input())

count = 0
for i in range(h+1):
    for j in range(60):
        for k in range(60):
            #매 시간 안에 '3'이 포함되어 있다면 카운트 증가
            if '3' in str(i) + str(j) + str(k):
                count += 1
print(count)

