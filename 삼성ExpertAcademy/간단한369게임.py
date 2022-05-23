N = input()
clap = ["3", "6", "9"]
for i in N:
    if i in clap:
        print('-', end=' ')
    else:
        print(i, end=' ')
