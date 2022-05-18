T = int(input())
answer = []
for i in range(T):
    arr = list(map(int, input().split()))
    answer.append(round(sum(arr) / 10))
    
for i in range(len(answer)):
    print("#"+str(i + 1)+" "+str(answer[i]))
