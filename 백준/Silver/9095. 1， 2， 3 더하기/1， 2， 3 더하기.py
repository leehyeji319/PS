#https://www.acmicpc.net/problem/9095
d = [0] * 11
d[1] = 1
d[2] = 2
d[3] = 4

for i in range(4, 11):
    d[i] = d[i - 3] + d[i - 2] + d[i - 1]

T = int(input())
for _ in range(T):
    N = int(input())
    print(d[N])