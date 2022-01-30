def solution(phone_book):
    answer = True
    num = sorted(phone_book)
    for i in range(len(phone_book) - 1):
        if num[i] == num[i + 1][:len(num[i])]:
            answer = False
    return answer

#print(solution(["123","456","789"]))
