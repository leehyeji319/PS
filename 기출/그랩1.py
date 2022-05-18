import math
def solution(n, text, second):
    answer = ''
    text = text.replace(' ', '_')
    line = math.floor(second / n)
    index = second % n
    
    if len(text) == n:
        if line % 2 == 0 and index != 0:
            underbar = "_" * (n - index)
            showstr = text[:index]
            answer = underbar + showstr
        elif line % 2 == 1 and index != 0:
            underbar = "_" * (index)
            showstr = text[index:]
            answer = underbar + showstr
        elif index == 0 and line % 2 == 1:
            answer = text[:n]
        elif index == 0 and line % 2 == 0:
            answer = "_" * n
        
        
    
    
    
    
    
    return answer
    
print(solution(6, "hi bye", 6))