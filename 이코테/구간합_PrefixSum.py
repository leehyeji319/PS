# Prefix Sum을 활용한 알고리즘 코드
# 데이터의 개수 N과 데이터 입력 받기
from sys import prefix


n = 5
data = [10, 20, 30, 40, 50]

#Prefix Sum 배열 계산
summary = 0
prefix_sum = [0]
for i in data:
    summary += i
    prefix_sum.append(summary)

# 구간 합 계산
left = 3
right = 4
print(prefix_sum[right] - prefix_sum[left - 1])