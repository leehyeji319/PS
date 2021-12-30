import sys
n = int(sys.stdin.readline())
l = []
result = [0 for _ in range(10001)]
for _ in range(n):
    num = int(sys.stdin.readline())
    result[num] += 1


for i in range(len(result)):
    for j in range(result[i]):
        print(i)

## 파이썬 메모리 초과가 나는 이유 ## 
# 모든 입력을 배열에 저장하면 당연히 메모리 초과가 된다. 문제의 메모리 제한은 겨우 8mb 
# 아무리 작은 자료형이라도 short형은 20mb 이다.
# input()은 아예 안되고, sys.stdin.readline() 이랑 sys.stdout.write 써야된다.
# 기본적으로 sort는 원소들의 비교를 통해 정렬을 수행하고 O(nlogn)의 시간복잡도이다
