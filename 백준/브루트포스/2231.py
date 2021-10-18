n = int(input())

for i in range(1, n + 1):
    #각 자릿수 합 구하기
    a = sum(map(int, str(i)))
    num = i + a
    if num == n:
        print(i)
        break
    if n == i:
        print(0)