from itertools import permutations

def is_prime_number(x):
    if x == 0 or x == 1:
        return False
    # 2부터 (x - 1)까지의 모든 수를 확인하며
    for i in range(2, x):
        # x가 해당 수로 나누어떨어진다면
        if x % i == 0:
            return False # 소수가 아님
    return True # 소수임

def solution(numbers):
    answer = []
    arr = []
    for i in range(len(numbers)):
        arr.append(numbers[i])
    
    for i in range(1, len(arr) + 1):
        tmp = list(map(''.join, permutations(arr, i)))
        for j in tmp:
            if j[0] == '0':
                continue
            num = int(j)
            if is_prime_number(num) == True:
                answer.append(num)
    a_set = set(answer)
    print(sorted(a_set))
    return len(a_set)

numbers = "1231" # 정답 18
print(solution(numbers))