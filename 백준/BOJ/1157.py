import collections

s = input()
s = s.upper()
answer = []
count = collections.Counter(s)
max_value = max(list(count.values()))
for key in list(count.keys()):
    if count[key] == max_value:
        answer.append(key)

if len(answer) != 1:
    print("?")
else:
    print(''.join(answer))