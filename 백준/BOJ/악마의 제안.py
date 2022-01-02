#수학 https://www.acmicpc.net/problem/23972
import math
k, n = map(int, input().split())
if n == 1:
    print(-1)
    exit(0)
x = k * n // (n - 1)
while (x - k) * n < x:
    x += 1
print(x)