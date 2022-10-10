def solution(numbers):
    answer = []

    for num in numbers:
        tobin = bin(num)[:2]
        sumbin = 0
        for b in tobin:
            sumbin += b
        if sumbin == len(tobin):
            answer.append(1)





    return answer

print(solution([7,5]))