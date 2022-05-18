T = int(input())
answer = []
for i in range(T):
    arr = list(map(int, input().split()))
    sum = 0
    for j in arr:
        if j % 2 == 1:
            sum += j
    answer.append(sum)
for i in range(len(answer)):
    print("#"+str(i + 1)+" "+str(answer[i]))
