import math
from collections import deque

def solution(progresses, speeds):
    answer = []
    leftover = []
    spentday = deque()
    cnt = 1
    for i in progresses:
        leftover.append(100 - i)
    for i in range(len(leftover)):
        spentday.append(math.ceil(leftover[i] / speeds[i]))

    while True:
        for i in range(1, len(spentday)):
            tmp = spentday[0]
            if tmp >= spentday[i]:
                cnt += 1
            elif tmp < spentday[i]:
                break
        answer.append(cnt)
        for j in range(cnt):
            spentday.popleft()
        cnt = 1
        if len(spentday) == 0:
            break
    return answer

print(solution([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1]))