N, M = map(int, input().split())
arr1 = []
for i in range(N):
    arr1.append(list(map(int, input().split())))
M, K = map(int, input().split())
arr2 = []
for i in range(M):
    arr2.append(list(map(int, input().split())))
    
c = [[0 for _ in range(K)] for _ in range(N)]

for n in range(N):
    for k in range(K):
       for m in range(M):
           c[n][k] += arr1[n][m] * arr2[m][k]
for i in c:
    for j in i:
        print(j, end=' ')
    print()   
        