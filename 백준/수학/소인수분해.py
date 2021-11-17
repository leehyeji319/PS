def factorization(x):
    arr = []
    d = 2
    while d <= x:
        if x % d == 0:
            arr.append(d)
            x /= d
        else:
            d = d + 1
    return arr
n = int(input())
r = factorization(n)
for i in r:
    print(i)