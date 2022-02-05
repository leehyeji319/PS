def solution(prices):
    answer = [0] * len(prices)
    stack = []
    
    
    for idx, price in enumerate(prices):
        # if len(stack) == 0:
        #     stack.append([price, idx])
        # else:
        #     while stack[-1][0] > price:
        #         answer[stack[-1][1]] = idx - stack[-1][1]
        #         stack.pop()                
        #     stack.append([price, idx])

        while len(stack) !=0 and stack[-1][0] > price:
            answer[stack[-1][1]] = idx - stack[-1][1]
            stack.pop()                
        stack.append([price, idx])
            
    for i in range(len(stack)):
        answer[stack[i][1]] = len(prices) - 1 - stack[i][1]
        
    return answer

print(solution([1, 2, 3, 2, 3]))