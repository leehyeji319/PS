n, m = 5, 5
data = [1, 2, 3, 4, 5]

result = 0
summary = 0
end = 0

#start를 차례대로 증가시키며 반복
for start in range(n):
    #end를 가능한 만큼 이동시키기
    while summary < m and end < n:
        summary += data[end]
        end += 1
    # 부분합이 m일때 카운트 증가
    if summary == m:
        result += 1
    summary -= data[start]
    
print(result)