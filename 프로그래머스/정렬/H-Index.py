def solution(citations):
    
    citations.sort()
    for i in range(len(citations)):
        if citations[i] >= len(citations) - i:
            return len(citations) - i
    return 0
    
    
print(solution([0, 1, 3, 5, 6]))