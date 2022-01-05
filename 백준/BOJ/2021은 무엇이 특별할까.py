# https://www.acmicpc.net/problem/24039
num = 1000
a = [False, False] + [True] * (num - 1)
primes = []
for i in range(2, num + 1):
    if a[i]:
        primes.append(i)
        for j in range(2*i, num+1, i):
            a[j] = False
n = int(input())
for i in range(0, len(primes) - 1):
    if primes[i] * primes[i + 1] > n:
        print(primes[i] * primes[i + 1])
        exit(0)
