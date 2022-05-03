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