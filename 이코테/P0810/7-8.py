# 떡볶이의 떡 짜르기 
# 적절한 높이를 찾을 때까지 이진 탐색을 수행하여 높이 H를 반복해서 조정하면 됩니다.
# 현재 이 높이로 자르면 조건을 만족할 수 있는가? 를 확인한 뒤에 조건의 만족여부에 따라서 탐색범위를 좁히면 된다
# 절단기의 높이는 0부터 10억까지 정수중 하나 
# 이렇게 큰 탐색범위를 보면 가장 먼저 이진탐색을 떠올려야 합니다.

#떡의 개수N과 요청한 떡의 길이 M을 입력받는다
n, m = list(map(int, input().split(' ')))
# 각 떡의 개별 높이 정보를 입력
array = list(map(int, input().split()))

# 이진탐색을 위한 시작점과 끝점 설정
start = 0
end = max(array)

# 이진탐색 수행
result = 0 
while(start <= end):
    total = 0 
    mid = (start + end) // 2
    for x in array:
        # 잘랐을 때의 떡의 양 계산
        if x > mid:
            total += x - mid 
    # 떡의 양이 부족한 경우 더 많이 자르기 (왼쪽 부분 탐색)
    if total < m:
        end = mid - 1
    # 떡의 양이 충분한 경우 덜 자르기(오른쪽 부분 탐색)
    else:
        result = mid # 최대한 덜 잘랐을 때가 정답이므로, 여기에서 result에 기록
        start = mid + 1

# 정답 출력
print(result)
