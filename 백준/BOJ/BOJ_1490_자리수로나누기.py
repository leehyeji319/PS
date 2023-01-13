N = input()
cnt = 0

ff = True
for i in range(len(N)):
    if int(N[i]) != 0:
        if int(N) % int(N[i]) != 0:
            ff = False
if ff:
    print(int(N))
    exit()

while True:
    for i in range(10 ** cnt):
        target_digits = N + ('0' * (cnt - len(str(i)))) + str(i)

        flag = True
        for i in range(len(N)):
            if int(N[i]) != 0:
                if int(target_digits) % int(N[i]) != 0:
                    flag = False

        if flag:
            print(int(target_digits))
            exit()
    cnt += 1





