def solution(n, lost, reserve):
    reserve_n = list(set(reserve) - set(lost))
    lost_n = list(set(lost) - set(reserve))
    result = n - len(lost_n)
    for i in lost_n:
        if i - 1 in reserve_n:
            result += 1
            reserve_n.remove(i - 1)
        elif i + 1 in reserve_n:
            result += 1
            reserve_n.remove(i + 1)
    return result
print(solution(5, [2, 4], [1, 3, 5]))