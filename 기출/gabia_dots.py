def solution(dots, lines):
    answer = 0
    diff_dots = [] # 점들의 간격들

    for i in range(len(dots) - 1):
        diff_dots.append(dots[i + 1] - dots[i])

    for i in diff_dots:
        if diff_dots[i] == 1:
            diff_dots[i] = 0

    diff_sum = sum(diff_dots)

    for i in range(len(lines)):
        if diff_sum <= 0:
            break
        l = lines.pop()
        diff_sum -= l
        answer += 1

    if diff_sum > 0:
        return -1
    else:
        return answer


print(solution(
[1, 3, 4, 6, 7, 10], [2, 2, 2, 2]))