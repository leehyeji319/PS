#https://programmers.co.kr/learn/courses/4008/lessons/72547
def solution(mylist):
    answer = []
    for i in len(mylist):
        a = mylist[i + 1] - mylist[i]
        answer.append(a)
    return answer


def solution(mylist):
    answer = []
    for number1, number2 in zip(mylist, mylist[1:]):
        answer.append(abs(number1 - number2))
    return answer

if __name__ == '__main__':
    mylist = [83, 48, 13, 4, 71, 11]
    print(solution(mylist))
# ※ 주의 zip 함수에 서로 길이가 다른 리스트가 인자로 들어오는 경우에는 길이가 짧은 쪽 까지만 이터레이션이 이루어집니다. 