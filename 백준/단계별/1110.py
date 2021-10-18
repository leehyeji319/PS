a = int(input())
n = a
cnt = 0

while True:
    b = n // 10 + n % 10
    c = n % 10 * 10 + b % 10
    n = c
    cnt += 1
    if c == a:
        break
        
print(cnt)