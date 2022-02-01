def solution(array, commands):
    answer = []
    tmp = []

    for x in range(len(commands)):
        i = commands[x][0]
        j = commands[x][1]
        k = commands[x][2]
        tmp = array[i - 1 : j]
        tmp.sort()
        a = tmp[k - 1]
        answer.append(a)
    return answer

print(solution([1, 5, 2, 6, 3, 7, 4], [[2, 5, 3], [4, 4, 1], [1, 7, 3]]))