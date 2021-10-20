n = int(input())
arr = list(map(int, input().split()))
result = 0
num = 0

arr.sort()

for i in arr:
    result += i
    num += result

print(num)