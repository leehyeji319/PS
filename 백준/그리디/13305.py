n = int(input())
distance = list(map(int, input().split()))
cost = list(map(int, input().split()))

result = 0
start = cost[0]

for i in range(len(cost) - 1):
    if cost[i] < start:
        result += cost[i] * distance[i]
        start = cost[i]
    else:
        result += start * distance[i]
print(result)