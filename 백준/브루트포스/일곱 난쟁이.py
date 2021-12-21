# 2309
arr = [int(input()) for i in range(9)]

total = sum(arr)

for i in range(8):
    for j in range(i + 1, 9):
        if 100 == total - (arr[i] + arr[j]):
            num1 = arr[i]
            num2 = arr[j]
arr.remove(num1)
arr.remove(num2)
arr.sort()
for i in arr:
    print(i)