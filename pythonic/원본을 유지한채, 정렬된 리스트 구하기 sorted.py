# 원본을 유지한채, 정렬된 리스트 구하기 - sorted
# 파이썬의 sort() 함수를 사용하면 리스트의 원소를 정렬할 수 있습니다. 이때, sort 함수는 원본의 멤버 순서를 변경하지요.
# 따라서 원본의 순서는 변경하지 않고, 정렬된 값을 구하려면 sort 함수를 사용할 수 없습니다.

# 이런 경우는 어떻게 해야 할까요?

# 다른 언어에서는..(또는 이 기능을 모르시는 분은)
# 보통 사람들은 deep copy와 sort 함수를 이용합니다.

list1 = [3, 2, 1]
list2 = [i for i in list1] # 또는 copy.deepcopy를 사용
list2.sort()
# 파이썬에서는
# 파이썬의 sorted를 사용해보세요. 반복문이나, deepcopy 함수를 사용하지 않아도 새로운 정렬된 리스트를 구할 수 있습니다.

list1 = [3, 2, 1]
list2 = sorted(list1)


# https://wikidocs.net/16038