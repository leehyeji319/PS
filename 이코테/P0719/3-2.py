#문제: 1이 될 때까지 : 문제설명

#n, k 을 공백을 기준으로 구분하여 입력받기 
n, k = map(int, input().split())

result = 0 

while True:
    #N이 k로 나누어 떨어지는 수가 될 때까지 빼기 
    target = (n // k) * k
    result += (n - target) #1을 빼는 연산횟수를 한번에 더해주기
    n = target
    #n이 k보다 작을 때(더 이상 나눌 수 없을때) 반복분 탈출
    if n < k:
        break
    #k로 나누기 
    result += 1
    n //= k

#마지막으로 남은 수에 대하여 1씩 빼기
result += (n - 1)
print(result)