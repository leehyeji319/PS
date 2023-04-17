def solution(name, yearning, photo):
    answer = []
    dict = {}

    for i in range(len(name)):
        dict[name[i]] = yearning[i]
    cnt = 0
    for i in range(len(photo)):
        for j in range(len(photo[i])):
            if photo[i][j] in name:
                cnt += dict[photo[i][j]]
        answer.append(cnt)
        cnt = 0

    return answer