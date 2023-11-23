# 백준 강의실 배정이랑 비슷한듯

import heapq
def time_format(time_arr):
    arr = []
    for time in time_arr:
        start, end = time[0], time[1]
        arr.append([int(start.split(":")[0]) * 60 + int(start.split(":")[1]), 
                    int(end.split(":")[0]) * 60 + int(end.split(":")[1]) + 10])
    
    arr.sort()
    return arr
    

def solution(book_time):
    answer = 1
    h = []
    book_times = time_format(book_time)
    for time in book_times:
        if not h:
            heapq.heappush(h, time[1])
            continue
        if time[0] >= h[0]:
            heapq.heappop(h)
        else:
            answer += 1
        heapq.heappush(h, time[1])
    
    
    return answer

print(solution([["15:00", "17:00"], ["16:40", "18:20"], ["14:20", "15:20"], ["14:10", "19:20"], ["18:20", "21:20"]]	))