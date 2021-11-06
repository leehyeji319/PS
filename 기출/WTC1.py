# 원소개수 맞춰주기
def solution(arr):
    answer = []
    num_count = []
    num_count.append(arr.count(1))
    num_count.append(arr.count(2))
    num_count.append(arr.count(3))

    max_num = max(num_count)

    for i in range(3):
        if num_count[i] < max_num:
            plus = max_num - num_count[i]
            answer.append(plus)
        else: answer.append(0)

    return answer

solution([1, 2, 3])