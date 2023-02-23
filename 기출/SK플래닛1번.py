def trans_time(time):
    hours_to_minutes = int(time[:2]) * 60
    total_ = hours_to_minutes + int(time[3:5])

    return total_


def solution(bakery_schedule, current_time, k):
    answer = -1
    current_minutes = trans_time(current_time)
    bread = 0
    for i in range(len(bakery_schedule)):
        if trans_time(bakery_schedule[i]) < current_minutes:
            continue
        bread += int(bakery_schedule[i].split(" ")[1])

        if bread >= k:
            answer = trans_time(bakery_schedule[i]) - current_minutes
            return answer

    if k > bread:
        return -1


# print(solution(["09:05 10", "12:20 5", "13:25 6", "14:24 5"], "12:05", 10))
