while True:
    arr = list(map(int, input().split()))
    arr.sort()
    if sum(arr) == 0:
        break;
    if arr[2] * arr[2] == (arr[0] * arr[0]) + (arr[1] * arr[1]):
        print("right")
    else:
        print("wrong")
    