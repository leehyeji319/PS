from collections import deque

n, w, l = map(int, input().split())  # 트럭수, 다리길이, 최대하중
weights = deque(list(map(int, input().split())))

bridge = deque([0] * w)

time = 0
complete_truck = 0

while complete_truck < n:
    time += 1
    if bridge.popleft() != 0:
        complete_truck += 1

    if sum(bridge) + weights[0] <= l:
        bridge.append(weights.popleft())
    else:
        bridge.append(0)

    if len(weights) == 0:
        time += w
        break

print(time)