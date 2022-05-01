def solution(people, tshirts):
    answer = 0
    people.sort()
    tshirts.sort()
    
    for p in range(len(people)):
        if people[p] in tshirts:
            del tshirts[tshirts.index(people[p])]
            answer += 1
        elif people[p] not in tshirts:
            tshirts = [i for i in tshirts if i > people[p]]
            if len(tshirts) > 0:
                answer += 1
                del tshirts[0]
    return answer
print(solution([2, 3, 4], [1, 2, 3]))