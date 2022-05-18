T = int(input())
for t in range(T):
    answer = 0
    arr = input()
    f = arr[0]
    for i in range(1, len(arr)):
        start = 0
        if arr[i] == f:
            end = i
            l = end - start
            while end + l < len(arr):
                if arr[start:end] != arr[end: end + l]:
                    break
                start = end
                end += l
            else:
                answer = l
                break

    print(f"#{t + 1} {answer}")