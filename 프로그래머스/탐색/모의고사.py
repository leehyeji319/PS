# https://programmers.co.kr/learn/courses/30/lessons/42840
def solution(answers):
    first = [1, 2, 3, 4, 5]
    second = [2, 1, 2, 3, 2, 4, 2, 5]
    third = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    
    first_a = second_a = third_a = 0
    for i, answer in enumerate(answers):
        if first[i%len(first)] == answer:
            first_a += 1
        if second[i%len(second)] == answer:
            second_a += 1
        if third[i%len(third)] == answer:
            third_a += 1
    
    a = []
    if max(first_a, second_a, third_a) == first_a:
        a.append(1)
    if max(first_a, second_a, third_a) == second_a:
        a.append(2)
    if max(first_a, second_a, third_a) == third_a:
        a.append(3)
    
    return a

# enumerate 쓰임 기억하기