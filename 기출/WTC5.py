# 격자에 숫자 채우기

def solution(rows, columns):
    arr = [[0 for _ in range(columns)] for _ in range(rows)]
    r = c = 0
    num = 1
    change = 0
    while True:
        if arr[r][c] == 0:
            change += 1
        elif r == 0 and c == 0:
            if num % 2 == 1:
                break
        arr[r][c] = num
        if change == rows*columns:
            break
        


        if num % 2 == 0:
            r = (r + 1) % rows
        else:
            c = (c + 1) % columns
        num += 1
    print(arr)
    return arr

solution(2, 3)