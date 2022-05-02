def solution(people, tshirts):

    tshirts.sort(reverse=True)
    people.sort(reverse=True)
    answer = 0

    p_i = 0
    t_i = 0
    while p_i != len(people) and t_i != len(tshirts):
        if tshirts[t_i] >= people[p_i]:
            t_i += 1
            answer += 1
        p_i += 1

    return answer