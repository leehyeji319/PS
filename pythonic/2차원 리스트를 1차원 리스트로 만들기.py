def solution(mylist):
    answer = []
    for i in range(len(mylist)):            # 세로 크기
        for j in range(len(mylist[i])):     # 가로 크기
            a = mylist[i][j]
            answer.append(a)
    return answer



my_list = [[1, 2], [3, 4], [5, 6]]
answer = []
for element in my_list:
    answer += element


my_list = [[1, 2], [3, 4], [5, 6]]

# 방법 1 - sum 함수
answer = sum(my_list, [])

# 방법 2 - itertools.chain
import itertools
list(itertools.chain.from_iterable(my_list))

# 방법 3 - itertools와 unpacking
import itertools
list(itertools.chain(*my_list))

# 방법 4 - list comprehension 이용
[element for array in my_list for element in array]

# 방법 5 - reduce 함수 이용 1
from functools import reduce
list(reduce(lambda x, y: x+y, my_list))

# 방법 6 - reduce 함수 이용 2
from functools import reduce
import operator
list(reduce(operator.add, my_list))


# 제한적으로 사용 가능한 방법
# 아래의 방법은 각 원소의 길이가 동일한 경우에만 사용 가능합니다.

# 방법 7 - numpy 라이브러리의 flatten 이용
import numpy as np
np.array(my_list).flatten().tolist()
# 예를 들어 다음과 같은 리스트는 편평하게 만들 수 있고

[[1], [2]]
[[1, 2], [2, 3], [4, 5]]
# 다음과 같이 같이 각 원소의 길이가 다른 리스트는 편평하게 만들 수 없습니다.

[['A', 'B'], ['X', 'Y'], ['1']]