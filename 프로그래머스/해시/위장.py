# https://programmers.co.kr/learn/courses/30/lessons/42578
def solution(clothes):
    answer = 0
    kinds = {}
    for i in clothes:
        if i[1] in kinds: # 딕셔너리에 해당 종류가 있다면
            kinds[i[1]].append([i[0]])  # 이미 있다면 해당 종류에 값 추가
        else:
            kinds[i[1]] = [i[0]] # 없다면 해당 종류로 키를 만들면서 값 추가
    
    answer = 1
    for k in kinds:
        answer *= len(kinds[k]) + 1
    
    answer -= 1 # 옷을 안입는 경우는 빼기
            
    return answer


# 다른사람의 풀이 
def solution(clothes):
    from collections import Counter
    from functools import reduce
    cnt = Counter([kind for name, kind in clothes])
    answer = reduce(lambda x, y: x*(y+1), cnt.values(), 1) - 1
    return answer
