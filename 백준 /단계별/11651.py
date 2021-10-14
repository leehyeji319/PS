import sys

n = int(input())
l = []
for _ in range(n):
    l.append(list(map(int, sys.stdin.readline().split())))

l.sort(key=lambda x:x[1])  # 중요해중요 ~!~
# 2차원 배열에서 열을 기준으로 오름차순 할때 람다식 이용
# arr.sort(key=lambda x:x[1])

for i in l:
    for j in i:
        print(j, end=' ')
    print()