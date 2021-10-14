import sys
from collections import Counter

n = int(input())
l = []
for _ in range(n):
    l.append(int(sys.stdin.readline()))

l.sort()

def mean(nums):
    return round(sum(nums)/len(nums))

def median(nums):
    nums.sort()
    mid = nums[len(nums)//2]

    return mid

def freq(nums): # 빈도수 
    mode_dict = Counter(nums)
    modes = mode_dict.most_common()

    if len(nums) > 1: 
        if modes[0][1] == modes[1][1]:
            mod = modes[1][0]  # 만약 빈도수가 같다면, 두번째 빈도수 출력
        else:
            mod = modes[0][0] # 같지 않다면 그냥 빈도수 많은거 출력
    else:
        mod = modes[0][0] # 1보다 작으면 그냥 빈도수 출력

    return mod

def scope(nums): # 범위
    return max(nums) - min(nums)


print(mean(l))
print(median(l))
print(freq(l))
print(scope(l))