def solution(cap, n, deliveries, pickups):
    answer = -1
    total_delivers = sum(deliveries)
    house_cnt = len(deliveries)

    while (total_delivers > 0):
        total_delivers - cap
        idx = house_cnt - 1
        now_handson = cap
        total_distance = 0
        while (now_handson > 0):
            if deliveries[idx] != 0:
                if deliveries[idx] <= now_handson:
                    now_handson -= deliveries[idx]
                    deliveries[idx] = 0
                else:
                    now_handson = 0
                    deliveries[idx] -= now_handson



    return answer

print(solution(4, 5, [1, 0, 3, 1, 2], [0, 3, 0, 4, 0]))