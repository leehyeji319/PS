from collections import defaultdict

def solution(genres, plays):
    answer = []
    dict = {}
    
    for i in range(len(genres)):
        if genres[i] in dict:
            dict[genres[i]] += plays[i]
        else: 
            dict[genres[i]] = plays[i]
    
    
    dict_s = sorted(dict.items(), key = lambda item: item[1], reverse = True)
        
    
    dict_g_p = defaultdict(list)
    
    num = 0
    for g, p in zip(genres, plays):
        dict_g_p[g].append((p, num))
        num += 1
        
    for g, p in dict_s:
        g_to_p = sorted(dict_g_p[g], key = lambda x : (-x[0], x[1]))[:2]
        for played, idx in g_to_p:
            answer.append(idx)
        
        
    return answer

print(solution(["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 800, 2500]))
