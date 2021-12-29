n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

def div(arr):
    s = 0
    for i in arr:
        s += sum(i)
    if s == 0:
        return [1, 0]
    elif s == len(arr) * len(arr):
        return [0, 1]
    else:
        p1, p2, p3, p4 = [], [], [] ,[]
        l = len(arr) // 2
        for i in range(l):
            p1.append(arr[i][0:l])
            p2.append(arr[i][l:])
            p3.append(arr[l+i][0:l])
            p4.append(arr[l+i][l:])
        a1 = div(p1)
        a2 = div(p2)
        a3 = div(p3)
        a4 = div(p4)
        result = [a1[i] + a2[i] + a3[i] + a4[i] for i in range(len(a1))]
        return result
r = div(arr)
for i in r:
    print(i)