from collections import deque

def solution(bridge_length, weight, truck_weights):
    q = deque()
    time = 0
    sum_q = sum(q)
    while True:
        if sum_q + truck_weights[0] <= weight:
            q.append(truck_weights[0])
            sum_q += truck_weights[0]
            truck_weights.pop(0)
            time += 1
                
            if len(q) == bridge_length:
                sum_q -= q[0]
                q.popleft()
        else:
            if len(q) == bridge_length:
                sum_q -= q[0]
                q.popleft()
                continue
            else: 
                q.append(0)
                time += 1
                
        if len(truck_weights) == 0 and len(q) != 0:
            time += bridge_length
            break
        elif len(truck_weights) == 0 and sum(q) == 0:
            break
        
    return time
        

#print(solution(100, 10, [10]))