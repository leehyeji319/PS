def solution(x):
    answer = True
    sum = 0
    x_a = [int(a) for a in str(x)]
    for i in x_a:
        sum += int(i)
    if x % sum != 0:
        answer = False
        
    return answer

print(solution(18))