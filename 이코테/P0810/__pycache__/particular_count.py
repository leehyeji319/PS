# 정렬된 배열에서 특정 수의 개수 구하기 
# N개의 원소를 포함하고 있는 수열이 오름차순으로 정렬되어 있습니다. 
# 이때 이 수열에서 x가 등장하는 횟수를 계산하세요.
# 단 이 문제는 시간복잡도 O(logN)으로 알고리즘을 설계하지 않으면 시간초과판정!

#문제해결
# 데이터가 정렬되어 있기때문에 이진탐색 수행 가능
# 특정 값이 등장하는 첫번째 위치와 마지막 위치를 찾아 위치 차이를 계산해 문제를 해결 할 수 있습니다. (bisect 관련)

from bisect import bisect_left, bisect_right

def count_by_range(array, left_value, right_value):
    right_index = bisect_right(array, right_value)
    left_index = bisect_left(array, left_value)
    return right_index - left_index

n, x = map(int, input().split()) #데이터의 개수 n 찾고자하는 값 x 입력받기
array = list(map(int, input().split())) # 전체 데이터 입력받기

# 값이 [x,x] 범위에 잇는 데이터의 개수 계산
count = count_by_range(array, x, x)

# 값이 x인 원소가 존재하지 않는다면
if count == 0:
    print(-1)
# 값이 x인 원소가 존재한다면
else:
    print(count)
