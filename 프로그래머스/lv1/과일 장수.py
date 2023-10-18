def solution(k, m, score):
    # k : 가장 비싼 사과 m: 한 상자에 담는 사과 개수 1점은 최하점
    answer = 0
    if len(score) < m:
        return answer
    score.sort(reverse=True)

    cnt = 0

    while cnt != len(score) // m:
        i = m * cnt
        if i + m > len(score):
            return answer
        answer += score[i + m - 1] * m
        cnt += 1

    return answer


print(solution(3, 4, [1, 2, 3, 1, 2, 3, 1]))
# print(solution(4, 3, [4, 1, 2, 2, 4, 4, 4, 4, 1, 2, 4, 2]))