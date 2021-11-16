def is_prime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True # False가 리턴되지 않고 for문을 빠져나왔다면 소수이므로 True 리턴 
n = int(input())
arr = list(map(int, input().split()))
cnt = 0
for x in arr:
    if x > 1:
        if is_prime(x) == True:
            cnt += 1
print(cnt)