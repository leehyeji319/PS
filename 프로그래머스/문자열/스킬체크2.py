def solution(absolutes, signs):
    sum = 0
    for num, s in zip(absolutes, signs):
        if s == True:
            sum += num
        else:
            sum -= num

    return sum

print(solution([4,7,12], [True,False,True]))