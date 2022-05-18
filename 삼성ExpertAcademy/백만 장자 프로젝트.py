T = int(input())
for t in range(T):
    n = int(input())
    arr = list(map(int, input().split()))
    tmp = []
    answer = 0
    
    start = 0
    end = 0
    
    while start < len(arr):
        m_i = arr.index(max(arr[start:]))
        end = m_i
        answer += (arr[end] * (end - start)) - sum(arr[start:end])
        start = end + 1
    
    print("#" + str(t + 1), answer)