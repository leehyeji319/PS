#레벨3 : 선후수 수강

from collections import defaultdict

def solution(s1, s2, k):
    answer = []

    check = defaultdict(list)
    graph = defaultdict(list)
    for a, b in zip(s1,s2):
        check[b].append(a)
        graph[a].append(b)

    stack = [k]
    subjects = []
    while stack:
        subject_list = stack.pop()
        for subject in check[subject_list]:
            if check[subject] == []:
                subjects.append(subject)
            else:
                stack.append(subject)
    subjects = list(set(subjects))

    finished = False

    while subjects and not finished:
        subjects.sort()
        
        for subject in subjects:
            if subject in answer:
                continue
            if check[subject] == []:
                subjects.remove(subject)
                answer.append(subject)
                if subject == k:
                    finished = True
                    break
                for s in graph[subject]:
                    if subject in check[s]:
                        check[s].remove(subject)
                    subjects.append(s)
                break
    
    return answer

print(solution(["A", "E", "B", "D", "B", "H", "F", "H", "C"], ["G", "C", "G", "F", "J", "E", "B", "F", "B"], "B"))