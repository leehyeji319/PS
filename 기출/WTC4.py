#연속된 배열의 개수

def solution(s):
    answer = []
    cnt = 1
    for i in range(len(s) - 1):
        if s[i] == s[i + 1]:
            cnt += 1
        else:
            answer.append(cnt)
            cnt = 1
    answer.append(cnt)

    if s[0] == s[-1]:
        answer[0] += answer[-1]
        del answer[-1]
    answer.sort()
            
    return answer

solution("wowwow")