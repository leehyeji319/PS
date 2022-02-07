def solution(n, times):
    answer = 0

    start = 1
    end = max(times) * n
    
    while(start < end):
        total = 0
        mid = (start + end) // 2
        
        for t in times:
            total += mid // t
        
        if total >= n:
            end = mid
        else:
            start = mid + 1
            
    answer = start
    return answer


print(solution(6, [7, 10]))