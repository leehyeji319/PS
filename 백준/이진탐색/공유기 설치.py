n, c = map(int, input().split())
arr = []
for _ in range(n):
    a = int(input())
    arr.append(a)
arr.sort()

start = 1
end = arr[-1] - arr[0]
result = 0 

while start <= end:
    mid = (start + end) // 2
    