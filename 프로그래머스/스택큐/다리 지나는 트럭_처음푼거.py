from collections import deque

bridge_length = 100
weight = 100
truck_weights = [10,10,10,10,10,10,10,10,10,10]

q = deque()
time = 0

while True:
    if sum(q) + truck_weights[0] <= weight:
        if len(q) < bridge_length:
            q.append(truck_weights[0])
            truck_weights.pop(0)
            time += 1
        elif len(q) == bridge_length:
            q.popleft()
            q.append(truck_weights[0])
            truck_weights.pop(0)
            time += 1
    else:
        if len(q) == bridge_length:
            q.popleft()
            continue
            time += 1
        else: 
            q.append(0)
            time += 1
            
    if len(truck_weights) == 0 and len(q) != 0:
        time += bridge_length
        break
    elif len(truck_weights) == 0 and sum(q) == 0:
        break
    
        

print(time)