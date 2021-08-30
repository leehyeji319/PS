# 우선순위 큐 : Prioirty Queue
# 우선순위가 가장 높은 데이터를 가장 먼저 삭제하는 자료구조.
# 구현하려면 힙을 사용  최소 힙(값이 낮은거부터), 최대 힙(값이 높은거부터)

# 힙 라이브러리 사용 예제 : 최소 힙
import heapq

# 오름차순 힙 정렬(Heap Sort)
def heapsort(iterable):
    h = []
    result = []
    # 모든 원소를 차례대로 힙에 삽입 
    for value in iterable:
        heapq.heappush(h, value) # 힙 푸시
    # 힙에 삽입된 모든 원소를 차례대로 꺼내어 담기
    for i in range(len(h)):
        result.append(heapq.heappop(h)) # 힙 팝
    return result

result = heapsort([1, 3, 5, 7, 9, 2, 4, 6, 8, 0])
print(result)