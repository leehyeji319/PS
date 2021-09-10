mylist = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
new_list = [[], [], []]

for i in range(len(mylist)):
    for j in range(len(mylist[i])):
        new_list[i].append(mylist[j][i])

#         python에서는
# 파이썬의 zip과 unpacking 을 이용하면 코드 한 줄로 리스트를 뒤집을 수 있습니다.

mylist = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
new_list = list(map(list, zip(*mylist)))

# https://docs.python.org/ko/3/library/functions.html?highlight=built%20function
