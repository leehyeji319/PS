# 공부 시간 계산 어플
def solution(log):
    sum = 0
    start = end = 0
    for i, time in enumerate(log):
        hour, min = time.split(':')
        time = int(hour) * 60 + int(min)
        if i % 2 == 0:
            start = time
        else:
            end = time
            if end - start < 5:
                continue
            elif end - start > 105:
                sum += 105
            else:
                sum += (end - start)
    hour, min = divmod(sum, 60)
    if hour < 10:
        hour = '0'+str(hour)
    else:
        hour = str(hour)
    result = hour + ':' + str(min)

    print(result)
    return result

solution(["08:30", "09:00", "14:00", "16:00", "16:01", "16:06", "16:07", "16:11"])