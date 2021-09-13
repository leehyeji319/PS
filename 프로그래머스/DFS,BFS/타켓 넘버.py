# https://programmers.co.kr/learn/courses/30/lessons/43165/solution_groups?language=python3&type=my

def solution(numbers, target):
    parents  = [0]
    for number in numbers:
        child = []
        for parent in parents:
            child.append(parent + number)
            child.append(parent - number)

        parents = child
    return parents.count(target)

    