list1 = ['1', '100', '33']
list2 = []
for value in list1:
    list2.append(int(value))

# 파이썬에서는
# 파이썬의 map을 사용하면 for 문을 사용하지 않고도 멤버의 타입을 일괄 변환할 수 있습니다.

list1 = ['1', '100', '33']
list2 = list(map(int, list1))