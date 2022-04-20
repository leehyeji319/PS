def solution(participant, completion):
    dict = {}
    for p in participant:
        if p in dict:
            dict[p] += 1
        else:
            dict[p] = 1
    
    for c in completion:
        if dict[c] == 1:
            del dict[c]
        else:
            dict[c] -= 1
    
    
    
    return list(dict.keys())[0]
    
    
    
print(solution(["leo", "kiki", "eden"], ["eden", "kiki"]))