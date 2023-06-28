from string import ascii_lowercase

def solution(s, skip, index):
    answer = ''
    
    l = list(ascii_lowercase)
    
    for i in s:
        tmp = 1
        for_idx = 0
        while True:
            n_s = l[(l.index(i) + tmp) % 26]
            if n_s not in skip:
                for_idx += 1
            
            tmp += 1
            
            if for_idx == index:
                answer += n_s
                break;
                
                
    
    
    return answer
