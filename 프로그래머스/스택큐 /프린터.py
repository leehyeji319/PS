def solution(priorities, location):
    answer = 0
    idx = 0
    cnt = 0
    l = len(priorities)
    m = max(priorities)
        
    while True:
        if priorities[idx % l] < m:
            idx += 1
        elif priorities[idx % l] == m:
            if idx % l == location:
                cnt += 1
                answer = cnt
                break
            else: 
                priorities[idx % l] = 0
                idx += 1
                cnt += 1
                
        m = max(priorities)
       
    return answer

print(solution([1, 1, 9, 1, 1, 1], 0))