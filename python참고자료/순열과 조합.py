# 순열과 조합 combinations, permutations
# iterable의 원소로 순열과 조합을 구하는 방법.
# ex. 1, 2, 3 의 숫자가 적힌 카드가 있을 때, 이 중 두장을 꺼내는 경우의 수 -> 12, 13, 21, 23, 31, 32
# 'A', 'B', 'C'로 만들 수 있는 경우의 수
# 순열은 permutation !!!
from itertools import permutations
from itertools import combinations
from itertools import combinations_with_replacement
import itertools
pool = ['A', 'B', 'C']
# pool = [1, 2, 3]
print(list(map(''.join, itertools.permutations(pool)))) #3개의 원소로 수열 만들기
print(list(map(''.join, itertools.permutations(pool, 2)))) #2개의 원소로 수열 만들기

print(list(map(''.join, combinations(pool, 2))))
# print(list(combinations(pool, 2)))
print(list(map(''.join, combinations_with_replacement(pool, 2))))


iterable1 = 'ABCD'
iterable2 = 'xy'
iterable3 = '1234'
print(list(itertools.product(iterable1, iterable2, iterable3)))