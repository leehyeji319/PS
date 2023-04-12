import heapq
def solution(N, coffee_times):
    answer = []
    coffee_times_ = []
    for i in range(len(coffee_times)):
        coffee_times_.append([coffee_times[i], i + 1])
    h = []

    for i in range(N):
        heapq.heappush(h, coffee_times_[i])

    cnt = N

    for i in range(len(coffee_times)):
        if len(h) > 0:
            hp = heapq.heappop(h)
            answer.append(hp[1])
            if cnt < len(coffee_times):
                heapq.heappush(h, [coffee_times_[cnt][0] + hp[0], cnt + 1])
                cnt += 1

    return answer


print(solution(
1, [100, 1, 50, 1, 1]))