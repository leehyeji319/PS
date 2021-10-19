n, k = map(int, input().split())
coin_types = []
result = 0
for _ in range(n):
    coin_types.append(int(input()))

coin_types.sort(reverse=True)
for coin in coin_types:
    result += k // coin
    k %= coin
print(result)