# 문자열로 이루어진 삼각형 120도 회전

def solution(time, plans):
    use_time = 0
    last = ''
    for plan in plans:
        use_time_ = 0
        start = plan[1]
        end = plan[2]

        if start[-2:] == "PM":
            start = int(start[:-2]) + 12
        else:
            start = int(start[:-2])

        if end[-2:] == "PM":
            end = int(end[:-2]) + 12
        else:
            end = int(end[:-2])

        if start < 18:
            use_time_ += (18 - start)
        if 13 < end:
            use_time_ += (end - 13)
        
        if use_time + use_time_ < time:
            use_time += use_time_
            last = plan[0]

    return last