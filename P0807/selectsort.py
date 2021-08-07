# 선택 정렬 코드 이중 포문으로 해결

array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(len(array)): # 매번 앞쪽으로 보내고자 가장 앞 쪽 원소의 위치 
    min_index = i # 가장 작은 원소의 인덱스 # 가장 앞쪽 원소가 가장 작은걸로 해놓고
    for j in range(i + 1, len(array)): # 선형 탐색 시작 
        if array[min_index] > array[j]: #현재 가장 작은 원소보다 더 작은 원소가 있다면 바꾸기
            min_index = j
    array[i], array[min_index] = array[min_index], array[i] # 스와프 연산을 한줄로 간단하게 표현
    #가장 앞쪽 원소와 가장 작은 원소를 서로 바꿔줄 수 있도록 하는거임
print(array)

#선택정렬 시간 복잡도 O(n2)