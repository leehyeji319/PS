n = input()
l = []
for i in n:
    l.append(int(i))

for i in sorted(l, reverse=True):
    print(i, end='')


