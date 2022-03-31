def n_queens(col, i):
    n = len(col) - 1
    if (promising(col, i)):
        if (i == n):
            print(col[1: n + 1])
        else:
            for j in range(1, n + 1):
                col[i + 1] = j
                n_queens(col, i + 1)

def promising(col, i):
    k = 1
    flag = True
    while (k < i and flag):
        #같은 열에 있거나, 같은 대각선에 있는지?
        if (col[i] == col[k] or abs(col[i] - col[k]) == (i - k)):
            flag = False
        k += 1 #모든 k를 체크해서 리턴
    return flag

n = 4
col = [0] * (n + 1)
n_queens(col, 0)
