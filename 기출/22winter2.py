

def isChange(arr, n, before):
    flag = True
    new_arr = arr[:(n//2)]
    new = []
    for i in range(len(new_arr)):
        new.append(new_arr[i][0])

    for i in range(len(new_arr)):
        if new[i] not in before:
            flag = False
            break

    return flag, new



def solution(n, student, point):
    answer = 0
    total = []

    for i in range(1, n + 1):
        total.append([i, 0])


    for s, p in zip(student, point):
        before = []
        #점수 분배 중
        for i in range(len(total)):
            if total[i][0] == s:
                total[i][1] += p
        for i in range(len(total) // 2):
            before.append(total[i][0])
        #정렬후
        total.sort(key=lambda x: (-x[1], x[0]))

        flag, new_arr = isChange(total, n, before)
        if not flag:
            answer += 1


    return answer

print(solution(6, [6,1,4,2,5,1,3,3,1,6,5], [3,2,5,3,4,2,4,2,3,2,2]))