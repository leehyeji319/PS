def solution(line):
    answer = ''

    stack = []
    for l in line:
        if len(stack) == 0:
            stack.append(l)
        elif len(stack) >=2 and stack[-1] == '*' and stack[-2] != l:
            stack.append(l)
        elif len(stack) >= 2 and stack[-1] == '*' and stack[-2] == l:
            continue
        elif stack[-1] != l:
            stack.append(l)
        elif stack[-1] == l:
            stack.append('*')
    for s in stack:
        answer += s

    return answer

print(solution("aaabaaabaaabbaaabbbaa"))
print(solution("aaabaaabaaabbaaabbbaa") == "a*ba*ba*b*a*b*a*")
# print(solution("aabbbccbbb"))
# print(solution("hellllllo"))
# print(solution("wonderful"))
