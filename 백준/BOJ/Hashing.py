n = int(input())
arr = list(map(str, input()))
sum = 0
for i in range(len(arr)):
    sum += (ord(arr[i]) - 96) * (31**i)

print(sum % 1234567891)