def solution(mylist):
    answer = []
    for i in mylist:
        if i % 2 == 0:
            answer.append(i*i)
    return answer

# 파이썬에서는 파이썬의 list comprehension을 사용하면 한 줄 안에 for문과 if 문을 한번에 처리할 수 있습니다
def solution(mylist):
    answer = [number**2 for number in mylist if number % 2 == 0]

