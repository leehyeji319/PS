from queue import PriorityQueue
from datetime import datetime, timedelta


def solution(booked, unbooked):
    work_time = timedelta(minutes=10)
    time_fmt = "%H:%M"

    customers = sorted(booked + unbooked)
    queue = PriorityQueue()
    finish_time = datetime.strptime(customers[0][0], time_fmt) + work_time
    answer = [customers[0][1]]
    i = 1
    while i != len(customers):
        arrival_time = datetime.strptime(customers[i][0], time_fmt)

        if arrival_time <= finish_time:
            queue.put((1 if customers[i] in booked else 2, customers[i]))
            i += 1
            continue
        if queue.empty():
            answer.append(customers[i][1])
            finish_time = arrival_time + work_time
            i += 1
            continue
        to_serve = queue.get()[1]
        answer.append(to_serve[1])
        finish_time += work_time

    while not queue.empty():
        answer.append(queue.get()[1][1])

    return answer




## 예약하면 일반 고객보다 먼저 처리
## 10분간 업무 처리

## 업무 처리 중에 새로 들어오면 예약 확인

from collections import deque

def hmToM(time):
    hour, minute = list(map(int, time.split(":")))
    hour = hour * 60
    return minute + hour

def solution(booked, unbooked):
    answer = []

    unionList = []
    for b in booked:
        time, name = b
        time = hmToM(time)
        unionList.append([time, time + 10, True, name])

    for b in unbooked:
        time, name = b
        time = hmToM(time)
        unionList.append([time, time + 10, False, name])

    unionList.sort(key = lambda x : x[0])

    ## 업무를 이제 처리 할거야
    q = deque(unionList)

    while(len(q) != 1):
        currentWork = q.popleft()
        startTime, endTime, book, name = currentWork

        nsT, neT, nb, nn = q[0]
        if(nb != book and nb == True and nsT in range(startTime, endTime)):
            q.popleft()
            answer.append(nn)
            q.appendleft(currentWork)

        else:
            answer.append(name)

    answer.append(q[-1][-1])

    return answer