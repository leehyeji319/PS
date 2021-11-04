# 1003
cnt0 = [1, 0]
cnt1 = [0, 1]

T = int(input())

for _ in range(T):
    n = int(input())

    if n == 0:
        print("1 0")
    elif n == 1:
        print("0 1")
    else:
        for i in range(2, n + 1):
            cnt0.append(cnt0[i - 1] + cnt0[i - 2])
            cnt1.append(cnt1[i - 1] + cnt1[i - 2])
        print(f"{cnt0.pop()} {cnt1.pop()}")
        cnt0 = [1, 0]
        cnt1 = [0, 1]