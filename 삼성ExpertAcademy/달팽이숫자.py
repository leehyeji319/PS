def make_outer(arr, st, length, num):
    #배열, 해당 사각형 시작 위치, 사각형 크기, 시작 숫자
    last = st + length - 1 #사각형 : (st, st) ~ (last, last)
    for c in range(st, last + 1): #해당 최외각 사각형에서 첫번째행 처리 -> (st, st)~(st, last)까지 작업
        arr[st][c] = num
        num += 1
    for r in range(st + 1, last + 1): # 해당 최외각 사각형에서 마지막 열을 처리 : (st, last)은 이미 차있음 -> (st + 1, 1)~(last, last)까지 작업
        arr[r][last] = num
        num += 1
    for c in range(last - 1, st - 1, -1): #해당 최외각 사각형에서 마지막 행을 처리 : (last, last)은 이미 차있음 -> (last, last - 1)~(last, st)까지 작업
        arr[last][c] = num
        num += 1
    for r in range(last - 1, st, -1): #해당 최외각 사각형에서 첫번째 열을 처리: (last, st), (st,st)은 이미 차있음 -> (last - 1, st) ~ (st + 1, st)까지 작업
        arr[r][st] = num
        num += 1
    return num

T = int(input())
for i in range(1, T + 1):
    n = int(input())

    snail = [[0 for j in range(n)] for i in range(n)]

    num, st = 1, 0
    while n > 0:
        num = make_outer(snail, st, n, num)
        n -= 2
        st += 1
    print("#" + str(i))
    for s in snail:
        print(' '.join(map(str, s)))
        