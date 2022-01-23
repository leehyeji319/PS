n = int(input())
cnt = 0
for i in range(1, n + 1):
    n_arr = list(map(int, str(i)))
    if i < 100:
        cnt += 1
    elif n_arr[0] - n_arr[1] == n_arr[1] - n_arr[2]:
        cnt += 1
print(cnt)
        
    