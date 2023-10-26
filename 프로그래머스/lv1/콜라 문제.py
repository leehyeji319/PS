# a: 마트에 주어야하는 병 수
# b: 빈병 a개를 가져다 주면 마트가 주는 콜라 병 수 b
# n: 상빈이가 가지고 있는 빈 병의 개수
def solution(a, b, n):
    answer = 0
    while n >= a:
        able, remain = divmod(n, a)
        answer += able * b
        n = (able * b) + remain
    return answer

print(solution(2, 1, 20))