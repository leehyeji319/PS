arr = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
s = input()
cnt = 0

for a in arr:
    if a in s:
        cnt += s.count(a)
        s = s.replace(a, " ")

s = s.replace(" ", "")
print(len(s) + cnt)
        