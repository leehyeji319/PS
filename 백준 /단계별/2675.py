n = int(input())
for _ in range(n):
    s = input()
    r = s[0]
    str = s[2:]

    for i in str:
        print(i * int(r), end='')
    print()