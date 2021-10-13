n = int(input())
list = []
for _ in range(n):
    num = int(input())
    list.append(num)

list.sort()
for i in list:
    print(i)
print()

