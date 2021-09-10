# https://programmers.co.kr/learn/courses/4008/lessons/12731
def solution(mylist):
    answer = ''
    for i in range(0, len(mylist) - 1):
        answer = mylist[i] + mylist[i + 1]
    return answer

# 파이썬에서는
# 파이썬의 str.join(iterable)을 사용하면 이 코드를 두 줄로 줄일 수 있습니다 .

my_list = ['1', '100', '33']
answer = ''.join(my_list)