import heapq

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    
    while len(scoville) >= 2: 
        # 최솟값 가져오기
        min_1 = heapq.heappop(scoville)
        
        if min_1 >= K: #최솟값이 k보다 크면 종료
            return answer
        else: # 두 번째로 작은 값 가져와서 합친 값을 힙에넣기
            min_2 = heapq.heappop(scoville)
            heapq.heappush(scoville, min_1 + (min_2 * 2 ))
            answer += 1
    if scoville[0] > K:
        return answer
    else:
        return -1

solution([1, 2, 3, 9, 10, 12], 7)