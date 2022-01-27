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
                priorities[idx % l] = 0
                idx += 1
                cnt += 1
                answer = cnt
            else: 
                priorities[idx % l] = 0
                idx += 1
                cnt += 1
                
        m = max(priorities)
        if sum(priorities) == 0:
            break
    
    return answer