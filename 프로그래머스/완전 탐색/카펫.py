def solution(brown, yellow):
    answer = []
    wh = brown // 2 + 2
    
    a = 1
    b = wh - a
    while True:
        if a * b == brown + yellow:
            break
        else:
            a += 1
            b -= 1
    
    if a > b:
        answer.append(a)
        answer.append(b)
    else: 
        answer.append(b)
        answer.append(a)
            
    
    return answer



print(solution(24,24))

# def solution(brown, yellow):
#     length = (brown // 2) + 2
#     for i in range(1, length):
#         if i * (length - i) == brown + yellow:
#             return [length - i, i]