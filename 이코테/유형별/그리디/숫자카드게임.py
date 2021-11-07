N, M = map(int, input().split())

result = 0
for _ in range(N):
    data = list(map(int, input().split()))
    min_value = min(data)
    # 가장 작은 수 중에서 큰수찾기
    result = max(result, min_value)
print(result)

