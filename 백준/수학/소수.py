m = int(input())
n = int(input())
prime = []
for x in range(m, n + 1):
    if x > 1:
        for i in range(2, x):
            if x % i == 0:
                break
        else:
            prime.append(x)
if len(prime) > 0:
    print(sum(prime))
    print(min(prime))
else:
    print(-1)
# 1