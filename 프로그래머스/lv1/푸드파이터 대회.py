def solution(food):
    answer = ''
    for i in range(1, len(food)):
        food_cnt = food[i] // 2
        for j in range(food_cnt):
            answer = answer + str(i)
    
    answer = answer + '0' +answer[::-1]

    return answer