# 곱집합(Cartesian product) 구하기 - product
# 이번 강의에서는 iterable으로 곱집합을 구하는 방법을 알아봅니다.

# 예시) 두 스트링 'ABCD', 'xy' 의 곱집합은 Ax Ay Bx By Cx Cy Dx Dy 입니다.

# 다른 언어에서는..(또는 이 기능을 모르시는 분은)
# 보통 사람들은 for 문을 이용해 두 iterable의 원소를 하나씩 곱해갑니다.

iterable1 = 'ABCD'
iterable2 = 'xy'
iterable3 = '1234'

for value1 in iterable1:
    for value2 in iterable2:
        for value3 in iterable3:
            print(value1, value2, value3)
# 파이썬에서는
# itertools.product를 이용하면, for 문을 사용하지 않고도 곱집합을 구할 수 있습니다.

import itertools

iterable1 = 'ABCD'
iterable2 = 'xy'
iterable3 = '1234'
print(list(itertools.product(iterable1, iterable2, iterable3)))