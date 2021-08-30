# 힙 라이브러리 사용 예제 : 최소 힙 

import heapq #최소힙을 제공하고 최대힙은 지원하지않음

# 오름차순 힙 정렬(Heap Sort)
def heapsort(iterable):
    h = []
    result = []
    # 모든 원소를 차례대로 힙에 삽입
    for value in iterable:
        heapq.heappush(h, -value) # 최대를 구하고싶으면 부호 값을 바꿔준다
    # 힙에 삽입된 모든 원소를 차례대로 꺼내어 담기
    for i in range(len(h)):
        result.append(-heapq.heappop(h)) # 여기도 부호값을 바꿔준다
    return result

result = heapsort([1, 3, 5, 7, 9, 2, 4, 6 ,8 ,0])
print(result)